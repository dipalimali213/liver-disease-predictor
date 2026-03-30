# 🧠 Liver Disease Prediction Web Application

A complete **end-to-end Machine Learning web application** that predicts
the likelihood of liver disease using patient clinical data.\
Built with a production-ready pipeline and deployed live on the cloud.

🚀 **Live Demo:** https://liver-disease-predictor.onrender.com

------------------------------------------------------------------------

## 📌 Project Overview

This project focuses on early detection of liver disease using **machine
learning techniques** applied to real-world medical data.

The application takes patient attributes such as bilirubin levels,
enzyme values, and protein ratios, and predicts whether the patient is
likely to have liver disease.

✔️ Built with real healthcare dataset\
✔️ End-to-end pipeline (Data → Model → Web App → Deployment)\
✔️ Fully deployed and accessible online

------------------------------------------------------------------------

## 🎯 Key Features

-   🔍 Predict liver disease risk with high accuracy\
-   📊 Uses clinical parameters (13+ features)\
-   ⚖️ Handles class imbalance using SMOTETomek\
-   🌐 Interactive web interface using Flask\
-   ☁️ Deployed on Render

------------------------------------------------------------------------

## 🧪 Machine Learning Approach

-   **Algorithm Used:** Random Forest Classifier\
-   **Dataset:** Liver patient dataset\
-   **Preprocessing:**
    -   Data cleaning & feature engineering\
    -   Feature scaling (StandardScaler)\
-   **Class Imbalance Handling:** SMOTETomek\
-   **Model Optimization:** Hyperparameter tuning

📈 **Performance:** - Accuracy: \~87%\
- ROC-AUC Score: \~0.94

------------------------------------------------------------------------

## 🏗️ Project Architecture

User Input → Flask App → Preprocessing → ML Model → Prediction → Output

------------------------------------------------------------------------

## 🛠️ Tech Stack

**Languages & Libraries** - Python\
- NumPy, Pandas\
- Scikit-learn\
- Imbalanced-learn

**Web Development** - Flask\
- HTML, CSS

**Deployment & Tools** - Git & GitHub\
- Render\
- Gunicorn

------------------------------------------------------------------------

## 📂 Project Structure

LIVER-DISEASE/\
├── Dataset/\
├── templates/\
├── static/\
├── app.py\
├── train.py\
├── liver_model_tuned.pkl\
├── liver_scaler.pkl\
├── requirements.txt\
├── Procfile\
└── README.md

------------------------------------------------------------------------

## ⚙️ Installation & Setup

git clone https://github.com/YOURUSERNAME/liver-disease-predictor.git\
cd liver-disease-predictor

python -m venv venv\
venv`\Scripts`{=tex}`\activate  `{=tex}

pip install -r requirements.txt

python app.py

------------------------------------------------------------------------

## 🌐 Deployment

Build Command:\
pip install -r requirements.txt

Start Command:\
gunicorn app:app

------------------------------------------------------------------------

## 👩‍💻 Author

**Dipali Mali**\
Final Year CSE (Data Science) Student

------------------------------------------------------------------------

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
