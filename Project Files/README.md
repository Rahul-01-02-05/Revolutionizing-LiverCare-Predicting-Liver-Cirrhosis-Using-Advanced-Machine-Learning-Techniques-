# Liver Cirrhosis Prediction

This project predicts liver disease using a Random Forest Classifier.

## 💻 Technologies Used
- Python
- Flask
- Streamlit
- scikit-learn
- pandas

## 🧠 How It Works
A model is trained using the Indian Liver Patient dataset and then used in both Flask and Streamlit apps.

## 🚀 How to Run

### 🔹 Flask App
```bash
cd liver_cirrhosis_prediction
python app.py
```
Open http://localhost:5000

### 🔹 Streamlit App
```bash
streamlit run app_streamlit.py
```
Open the link provided in terminal (usually http://localhost:8501)

## 📁 Files
- `app.py` : Flask backend
- `app_streamlit.py` : Streamlit frontend
- `liver_disease_model.pkl` : Trained model
- `templates/index.html` : HTML form for Flask
