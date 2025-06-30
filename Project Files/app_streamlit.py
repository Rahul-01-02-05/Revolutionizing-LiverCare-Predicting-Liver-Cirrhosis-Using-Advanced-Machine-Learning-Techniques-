import streamlit as st
import numpy as np
import pickle

st.title("🧠 Liver Disease Prediction")
model = pickle.load(open('liver_disease_model.pkl', 'rb'))

age = st.number_input("Age", min_value=1.0, max_value=100.0, value=45.0)
gender = st.radio("Gender", ["Male", "Female"])
gender = 1.0 if gender == "Male" else 0.0
tb = st.number_input("Total Bilirubin", value=1.0)
db = st.number_input("Direct Bilirubin", value=0.5)
ap = st.number_input("Alkaline Phosphatase", value=200.0)
aa = st.number_input("Alamine Aminotransferase", value=50.0)
asa = st.number_input("Aspartate Aminotransferase", value=70.0)
tp = st.number_input("Total Proteins", value=6.5)
alb = st.number_input("Albumin", value=3.5)
agr = st.number_input("Albumin & Globulin Ratio", value=1.0)

if st.button("Predict"):
    features = np.array([[age, gender, tb, db, ap, aa, asa, tp, alb, agr]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Prediction: Liver Disease Detected")
    else:
        st.success("✅ Prediction: No Liver Disease")
