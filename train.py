"""
Run this file FIRST — it trains the model and saves:
  - liver_model_tuned.pkl
  - liver_scaler.pkl

Command: python train.py
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score
from imblearn.combine import SMOTETomek

print("Step 1: Loading dataset...")
df = pd.read_csv('Dataset/Liver_data.csv')
print(f"  Loaded {df.shape[0]} rows, {df.shape[1]} columns")

print("Step 2: Cleaning data...")
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(
    df['Albumin_and_Globulin_Ratio'].median()
)

print("Step 3: Encoding...")
df['Gender']  = np.where(df['Gender'] == 'Male', 1, 0)
df['Dataset'] = df['Dataset'].map({1: 1, 2: 0})

print("Step 4: Feature engineering...")
df['AST_ALT_Ratio']       = df['Aspartate_Aminotransferase'] / (df['Alamine_Aminotransferase'] + 1e-6)
df['Log_Total_Bilirubin'] = np.log1p(df['Total_Bilirubin'])
df['Log_Direct_Bilirubin']= np.log1p(df['Direct_Bilirubin'])
df['Age_Group']           = pd.cut(df['Age'], bins=[0,30,45,60,100], labels=[0,1,2,3]).astype(int)

features = [
    'Age', 'Gender',
    'Total_Bilirubin', 'Log_Total_Bilirubin', 'Log_Direct_Bilirubin',
    'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase',
    'AST_ALT_Ratio', 'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio', 'Age_Group'
]

X = df[features]
y = df['Dataset']

print("Step 5: Balancing classes with SMOTETomek...")
smote = SMOTETomek(random_state=42)
X_res, y_res = smote.fit_resample(X, y)
print(f"  Before: {dict(y.value_counts())} → After: {dict(pd.Series(y_res).value_counts())}")

print("Step 6: Train/test split...")
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.2, random_state=42, stratify=y_res
)

print("Step 7: Scaling features...")
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

print("Step 8: Training RandomForest...")
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_sc, y_train)

print("Step 9: Evaluating...")
y_pred = model.predict(X_test_sc)
y_prob = model.predict_proba(X_test_sc)[:, 1]
acc = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_prob)
print(f"\n  Accuracy : {acc*100:.1f}%")
print(f"  ROC AUC  : {auc:.4f}")
print()
print(classification_report(y_test, y_pred, target_names=['No Disease', 'Liver Disease']))

print("Step 10: Saving model and scaler...")
pickle.dump(model,  open('liver_model_tuned.pkl', 'wb'))
pickle.dump(scaler, open('liver_scaler.pkl', 'wb'))

print("\n  liver_model_tuned.pkl  — saved")
print("  liver_scaler.pkl       — saved")
print("\nDone! Now run: python app.py")
