from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('liver_disease_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        gender = float(request.form['gender'])
        tb = float(request.form['tb'])
        db = float(request.form['db'])
        ap = float(request.form['ap'])
        aa = float(request.form['aa'])
        asa = float(request.form['asa'])
        tp = float(request.form['tp'])
        alb = float(request.form['alb'])
        agr = float(request.form['agr'])

        features = np.array([[age, gender, tb, db, ap, aa, asa, tp, alb, agr]])
        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "⚠️ Liver Disease Detected"
        else:
            result = "✅ No Liver Disease"

        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"❌ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
