from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('liver_model_tuned.pkl', 'rb'))
scaler = pickle.load(open('liver_scaler.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age         = int(request.form['Age'])
        gender      = 1 if request.form['Gender'] == 'Male' else 0
        t_bili      = float(request.form['Total_Bilirubin'])
        d_bili      = float(request.form['Direct_Bilirubin'])
        alk_phos    = int(request.form['Alkaline_Phosphotase'])
        alt         = int(request.form['Alamine_Aminotransferase'])
        ast         = int(request.form['Aspartate_Aminotransferase'])
        tot_prot    = float(request.form['Total_Protiens'])
        albumin     = float(request.form['Albumin'])
        ag_ratio    = float(request.form['Albumin_and_Globulin_Ratio'])

        ast_alt_ratio   = ast / (alt + 1e-6)
        log_t_bili      = np.log1p(t_bili)
        log_d_bili      = np.log1p(d_bili)
        age_group       = min(3, int((age - 1) // 30))

        features = np.array([[
            age, gender, t_bili, log_t_bili, log_d_bili,
            alk_phos, alt, ast, ast_alt_ratio,
            tot_prot, albumin, ag_ratio, age_group
        ]])

        features_scaled = scaler.transform(features)
        prediction      = model.predict(features_scaled)[0]
        probability     = round(model.predict_proba(features_scaled)[0][1] * 100, 1)

        result = 'Liver Disease Detected' if prediction == 1 else 'No Liver Disease'
        risk   = 'high' if prediction == 1 else 'low'

        return render_template('result.html',
                               result=result,
                               probability=probability,
                               risk=risk,
                               age=age,
                               gender=request.form['Gender'])
    except Exception as e:
        return render_template('result.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
