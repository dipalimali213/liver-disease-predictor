# 🧠 Liver Disease Prediction using Machine Learning

## 📌 Project Abstract

"A Comparative Analysis of Machine Learning Algorithms for Early
Prediction of Liver Disease"

By\
1. Sonawane Harshada Ravindra (221106021, 23)\
2. Mali Dipali Vilas (221106055, 55)\
3. Narkhede Sanjana Nitin (231206003, 64)

Under the Guidance of\
Prof. Dr. P. S. Sanjekar

This project presents a comparative study of machine learning algorithms
to predict liver disease at an early stage using clinical data. The
system analyzes various health parameters and helps in identifying
potential liver disease risk.

------------------------------------------------------------------------

## 📌 Project Overview

The aim of this project is to build a machine learning model that
predicts liver disease based on patient medical attributes.

The model uses clinical features such as: - Age\
- Gender\
- Bilirubin levels\
- Liver enzyme levels\
- Protein levels

------------------------------------------------------------------------

## ⚙️ Working (Up to Model)

1.  Data Collection\

-   Dataset containing liver patient records

2.  Data Preprocessing\

-   Handling missing values\
-   Encoding categorical variables\
-   Feature scaling using StandardScaler

3.  Handling Imbalanced Data\

-   Applied SMOTETomek technique

4.  Model Training\

-   Random Forest\
-   Logistic Regression\
-   Decision Tree

5.  Model Evaluation\

-   Accuracy\
-   ROC-AUC Score

6.  Model Selection\

-   Best model selected based on performance

7.  Model Saving\

-   liver_model_tuned.pkl\
-   liver_scaler.pkl

------------------------------------------------------------------------

## 🧪 Machine Learning Details

-   Algorithm: Random Forest Classifier\
-   Class Imbalance Handling: SMOTETomek\
-   Feature Scaling: StandardScaler

Performance: - Accuracy: \~87%\
- ROC-AUC Score: \~0.94

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
