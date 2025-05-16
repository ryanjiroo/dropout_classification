import streamlit as st
import pandas as pd
import joblib
import urllib.request
import io

# Load model dari raw GitHub URL
url = 'https://raw.githubusercontent.com/ryanjiroo/dropout_classification/main/rf_model.pkl'
response = urllib.request.urlopen(url)
model_file = io.BytesIO(response.read())
loaded_rf_model = joblib.load(model_file)

# OPTIONAL: load the label encoder if class labels were encoded
# label_encoder = joblib.load('label_encoder.pkl')

# Define top 5 features (same order as used during training)
top_5_features = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date'
]

# Streamlit UI
st.title("🎓 Student Status Prediction App")

st.write("Isi data berikut untuk memprediksi status mahasiswa:")

# Input fields
cu1_approved = st.number_input("Curricular Units 1st Semester Approved", min_value=0, value=10)
cu1_grade = st.number_input("Curricular Units 1st Semester Grade", min_value=0.0, max_value=20.0, value=14.5)
cu2_approved = st.number_input("Curricular Units 2nd Semester Approved", min_value=0, value=12)
cu2_grade = st.number_input("Curricular Units 2nd Semester Grade", min_value=0.0, max_value=20.0, value=15.0)
tuition_up_to_date = st.selectbox("Tuition Fees Up-to-Date?", options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

# Prediction
if st.button("Predict Status"):
    # Susun dictionary mengikuti urutan yang benar
    new_data_dict = {
        'Curricular_units_2nd_sem_approved': [cu2_approved],
        'Curricular_units_1st_sem_approved': [cu1_approved],
        'Curricular_units_2nd_sem_grade': [cu2_grade],
        'Curricular_units_1st_sem_grade': [cu1_grade],
        'Tuition_fees_up_to_date': [tuition_up_to_date]
    }

    new_data_df = pd.DataFrame(new_data_dict)

    # Tidak perlu reindex karena kita sudah atur sesuai urutan
    prediction_numeric = loaded_rf_model.predict(new_data_df)

    # Mapping hasil prediksi numerik ke label
    if prediction_numeric[0] == 2:
        predicted_status = "Graduate"
    elif prediction_numeric[0] == 1:
        predicted_status = "Dropout"
    else:
        predicted_status = "Enrolled"

    st.success(f"🎯 Predicted Student Status: **{predicted_status}**")
