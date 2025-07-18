# 🧠 Diabetes Prediction Web App

A simple Streamlit web application that predicts whether a person is likely to have diabetes based on their health metrics using a trained machine learning model.

👉 **Live App**: [Click here to use the Diabetes Predictor](https://diabetes-predictor-y3z4wafk2ntsnjbehcvorc.streamlit.app/)

---

## 🚀 How It Works

This application takes user input for various medical parameters and uses a trained machine learning model (based on the **PIMA Indian Diabetes Dataset**) to predict the likelihood of diabetes.

### 🔍 User Inputs:
- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

Once the user fills in the values and clicks **Predict**, the app shows whether the person is **Diabetic** or **Not Diabetic**.

---

## 🧾 Project Structure

| File                          | Description                                                                 
|------------------------------|-----------------------------------------------------------------------------
| `DiabetesPredictionWebApplication.py` | The main Streamlit app that builds the UI and handles user input/output. 
| `predictive_system.py`       | Handles model loading and prediction logic in a reusable function.         
| `trained_model.sav`          | The serialized (`.sav`) trained ML model (usually from `sklearn`).         
| `requirements.txt`           | List of required Python packages to run the app on Streamlit Cloud.        

---

## 🛠 Technologies Used

- Python
- Streamlit
- scikit-learn
- Pandas
- NumPy
- Pickle (for model serialization)

---

## 📦 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/rahulAdithya0207/diabetes-predictor.git
cd diabetes-predictor

# (Optional) Create and activate virtual environment
conda create -n diabetes_app python=3.10 -y
conda activate diabetes_app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run DiabetesPredictionWebApplication.py
