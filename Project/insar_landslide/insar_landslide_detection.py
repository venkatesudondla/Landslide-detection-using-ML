import numpy as np
import rasterio
from rasterio.features import shapes
from shapely.geometry import shape
import geopandas as gpd
from rasterio.mask import mask as rio_mask
import matplotlib.pyplot as plt
import os

# ----------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------

# Input InSAR velocity raster (GeoTIFF)
# INSAR_TIF = "insar_velocity.tif" 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSAR_TIF = os.path.join(BASE_DIR, "insar_velocity.tif")  # Change if needed

# Optional DEM-derived slope raster
SLOPE_TIF = "None"            # Set to None if not available

# Output file
OUTPUT_GEOJSON = "landslide_zones_insar.geojson"

# Landslide threshold
# Example: pixels moving faster than -20 mm/year (downslope motion)
VEL_THRESHOLD = 200

# Minimum slope angle
MIN_SLOPE = 10

# ----------------------------------------------------
# LOAD INSAR VELOCITY DATA
# ----------------------------------------------------

print("Loading InSAR velocity file...")

with rasterio.open(INSAR_TIF) as src:
    vel = src.read(1).astype(float)
    profile = src.profile
    transform = src.transform
    crs = src.crs
    print("Velocity stats -> min:", np.nanmin(vel), "max:", np.nanmax(vel))


nodata = profile.get("nodata", None)
if nodata is not None:
    vel[vel == nodata] = np.nan

# ----------------------------------------------------
# LOAD OPTIONAL SLOPE DATA
# ----------------------------------------------------

slope = None
if SLOPE_TIF is not None and os.path.exists(SLOPE_TIF):
    print("Loading slope raster...")
    with rasterio.open(SLOPE_TIF) as ssrc:
        slope = ssrc.read(1).astype(float)
        s_nodata = ssrc.profile.get("nodata", None)
        if s_nodata is not None:
            slope[slope == s_nodata] = np.nan

# ----------------------------------------------------
# MASKING INVALID PIXELS
# ----------------------------------------------------

print("Applying masks...")

mask_valid = ~np.isnan(vel)

if slope is not None:
    mask_valid &= ~np.isnan(slope)
    mask_valid &= (slope >= MIN_SLOPE)

vel_masked = np.where(mask_valid, vel, np.nan)

# ----------------------------------------------------
# LANDSLIDE DETECTION (THRESHOLD METHOD)
# ----------------------------------------------------

print("Detecting landslide candidate pixels...")

landslide_pixels = (vel_masked >= VEL_THRESHOLD)
landslide_pixels &= mask_valid

print(f"Total landslide candidate pixels: {landslide_pixels.sum()}")

# ----------------------------------------------------
# VECTORIZE LANDSLIDE PIXELS TO POLYGONS
# ----------------------------------------------------

print("Converting pixels to polygons...")

landslide_int = landslide_pixels.astype(np.uint8)

results = []
for geom, value in shapes(landslide_int, mask=landslide_pixels, transform=transform):
    if value == 1:
        results.append(shape(geom))

if not results:
    print("No landslide polygons detected! Try lowering the threshold.")
    exit()

gdf = gpd.GeoDataFrame(geometry=results, crs=crs)

# ----------------------------------------------------
# ADD AVERAGE VELOCITY FOR EACH POLYGON
# ----------------------------------------------------

print("Computing average deformation for each polygon...")

avg_vel_list = []
for poly in gdf.geometry:
    try:
        out_image, _ = rio_mask(
            rasterio.open(INSAR_TIF),
            [poly.__geo_interface__],
            crop=True
        )
        arr = out_image[0].astype(float)
        if nodata is not None:
            arr[arr == nodata] = np.nan
        avg_vel = np.nanmean(arr)
    except Exception:
        avg_vel = np.nan

    avg_vel_list.append(avg_vel)

gdf["avg_velocity"] = avg_vel_list

# ----------------------------------------------------
# SAVE OUTPUT
# ----------------------------------------------------

gdf.to_file(OUTPUT_GEOJSON, driver="GeoJSON")
print(f"Saved landslide polygons to: {OUTPUT_GEOJSON}")

# ----------------------------------------------------
# VISUALIZATION
# ----------------------------------------------------

print("Displaying map...")

plt.figure(figsize=(8, 6))
plt.imshow(vel, cmap="jet")
plt.colorbar(label="Velocity (mm/year)")
plt.title("InSAR Velocity Map")

ys, xs = np.where(landslide_pixels)
plt.scatter(xs, ys, s=1, color='black')
plt.show()
