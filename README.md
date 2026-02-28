# Landslide-detection-using-ML
# 🌍 Landslide Detection Using Machine Learning

A Machine Learning-based predictive system designed to detect potential landslide occurrences using environmental and geological data. The model analyzes parameters such as rainfall, soil moisture, slope angle, and other terrain-related features to classify landslide risk levels.

The core objective of this project is **early risk prediction and disaster prevention using data-driven techniques**.

---

## 📌 Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Dataset](#dataset)  
- [Model Evaluation](#model-evaluation)  
- [Project Structure](#project-structure)  
- [Future Enhancements](#future-enhancements)  
- [Author](#author)  

---

## 🚀 Features

- Data preprocessing and cleaning  
- Feature selection and engineering  
- Supervised Machine Learning models  
- Landslide risk classification (Low / Moderate / High)  
- Model performance evaluation  
- Visualization of results and insights  

---

## 🛠️ Tech Stack

| Component | Technology / Framework |
|-----------|------------------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Model Saving | Joblib / Pickle |

---

## ⚡ Quick Start Guide

Follow these steps to quickly set up and run the Landslide Detection Using Machine Learning project:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/venkatesudondla/landslide-detection-ml.git
cd landslide-detection-ml
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

- **Windows**
```bash
venv\Scripts\activate
```

- **Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare Dataset

- Place the InSAR-based dataset file inside the `data/` folder  
- Ensure the file name matches the one used in `train_model.py`

Example:

```
data/insar_landslide_dataset.csv
```

### 5️⃣ Train the Model

```bash
python models/train_model.py
```

This will:
- Preprocess the dataset  
- Train the ML model  
- Save the trained model as `saved_model.pkl`

### 6️⃣ Run Prediction

```bash
python models/predict.py
```

### 7️⃣ (Optional) Run Web Application

If a dashboard is included:

```bash
python app.py
```

Then open your browser:

```
http://localhost:5000
```

---

You are now ready to test and evaluate the Landslide Detection ML system 🚀
```

---

## 📊 Dataset

The dataset used in this project is derived from **InSAR (Interferometric Synthetic Aperture Radar) satellite data**, which is widely used for monitoring ground surface deformation and slope instability.

InSAR technology enables the detection of minute ground movements by analyzing phase differences between satellite radar images captured at different time intervals. This makes it highly suitable for identifying early signs of landslides and terrain displacement.

### 🌍 Data Source

- Satellite-based InSAR observations  
- Ground surface displacement measurements  
- Terrain and environmental parameters combined with satellite data  

### 📌 Features Included

The dataset contains environmental and terrain-related parameters such as:

- Rainfall intensity  
- Soil moisture level  
- Slope angle  
- Soil type  
- Surface displacement (from InSAR data)  
- Historical landslide occurrence (label/output variable)  

### 🧹 Data Preprocessing Steps

Before training the Machine Learning models, the following preprocessing steps were performed:

- Handling missing and inconsistent values  
- Removing noise from satellite displacement measurements  
- Normalization / Standardization of numerical features  
- Feature scaling  
- Encoding categorical variables (if applicable)  
- Train-test split for model evaluation  

The integration of satellite-based deformation data with environmental parameters improves the accuracy and reliability of landslide risk prediction.

---

## 📈 Model Evaluation

The following Machine Learning algorithms are implemented:

- Logistic Regression  
- Decision Tree  
- Random Forest  
- Support Vector Machine (SVM)  

Model performance is evaluated using:

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  

The best-performing model is selected based on overall evaluation metrics.

---

## 📁 Project Structure

```
landslide-detection-ml/
│
├── data/
│   ├── raw_data.csv
│   └── processed_data.csv
│
├── models/
│   ├── train_model.py
│   ├── predict.py
│   └── saved_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📈 Future Enhancements

- Integration with real-time environmental data  
- Deep learning models (ANN / LSTM)  
- Hyperparameter tuning optimization  
- Deployment using cloud platforms  
- Web-based interactive dashboard  

---

---

## 📜 License

This project is developed for academic and research purposes.

