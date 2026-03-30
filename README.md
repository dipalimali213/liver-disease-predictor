# Liver Disease Prediction using Machine Learning

## 📌 Project Abstract

**"A Comparative Analysis of Machine Learning Algorithms for Early Prediction of Liver Disease"**

**By**  
1. Sonawane Harshada Ravindra (221106021, 23)  
2. Mali Dipali Vilas (221106055, 55)  
3. Narkhede Sanjana Nitin (231206003, 64)  

**Under the Guidance of**  
Prof. Dr. P. S. Sanjekar  

This project presents a comparative analysis of multiple machine learning algorithms to enable early prediction of liver disease using clinical data. The system processes various medical attributes and identifies patterns associated with liver disorders, helping in early diagnosis and decision support.

---

## 📌 Project Overview

Liver disease is a critical health issue that often goes undetected in early stages. This project aims to build a **predictive machine learning model** that can classify whether a patient is likely to have liver disease based on diagnostic parameters.

The system is trained on real-world patient data and focuses on improving prediction accuracy through preprocessing, feature engineering, and handling class imbalance.

### 🔍 Input Features
- Age  
- Gender  
- Total Bilirubin  
- Direct Bilirubin  
- Alkaline Phosphotase  
- ALT (Alanine Aminotransferase)  
- AST (Aspartate Aminotransferase)  
- Total Proteins  
- Albumin  
- Albumin/Globulin Ratio  

---

## ⚙️ Methodology (Working up to Model)

### 1. Data Collection
- Liver disease dataset containing patient medical records  
- Includes both diseased and non-diseased cases  

### 2. Data Preprocessing
- Handling missing or inconsistent values  
- Encoding categorical variables (e.g., Gender)  
- Feature scaling using **StandardScaler**  

### 3. Handling Imbalanced Data
- Dataset had class imbalance  
- Applied **SMOTETomek** to:
  - Oversample minority class  
  - Remove noisy samples  

### 4. Model Training
Multiple algorithms were implemented for comparison:
- Random Forest Classifier  
- Logistic Regression  
- Decision Tree  

### 5. Model Evaluation
Models were evaluated using:
- Accuracy  
- ROC-AUC Score  
- Confusion Matrix  

### 6. Model Selection
- Random Forest provided the best performance  
- Selected as final model  

### 7. Model Saving
- Trained model saved as:
  - `liver_model_tuned.pkl`  
  - `liver_scaler.pkl`  

---

## 🧪 Machine Learning Details

- **Final Algorithm:** Random Forest Classifier  
- **Class Imbalance Technique:** SMOTETomek  
- **Feature Scaling:** StandardScaler  

### 📊 Performance Metrics
- Accuracy: ~87%  
- ROC-AUC Score: ~0.94  

---

------------------------------------------------------------------------

## 📂 Project Structure

LIVER-DISEASE/\
├── Dataset/\
├── train.py\
├── liver_model_tuned.pkl\
├── liver_scaler.pkl\
└── README.md

------------------------------------------------------------------------

## ▶️ How to Run

python train.py

------------------------------------------------------------------------

## 👩‍💻 Author

Dipali Mali\
Final Year CSE (Data Science) Student

------------------------------------------------------------------------

## ⭐ Note

This project is developed for educational and research purposes.
