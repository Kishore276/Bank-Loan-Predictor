import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('./Model/ML_Model.pkl', 'rb'))

def run():
    img1 = Image.open('bank.png')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("Bank Loan Prediction using Machine Learning")

    # Gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x], help="Select applicant's gender.")

    # Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x], help="Is the applicant married?")

    # Dependents
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents", dep_options, format_func=lambda x: dep_display[x], help="Number of dependents.")

    # Education
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x], help="Applicant's education level.")

    # Employment Status
    emp_display = ('Job','Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x], help="Applicant's employment type.")

    # Property Area
    prop_display = ('Rural','Semi-Urban','Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x], help="Area where the property is located.")

    # Credit Score
    cred_display = ('Between 300 to 500','Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x], help="Applicant's credit score range.")

    # Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)", min_value=0, help="Enter applicant's monthly income.")

    # Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", min_value=0, help="Enter co-applicant's monthly income.")

    # Loan Amount
    loan_amt = st.number_input("Loan Amount", min_value=1, help="Enter desired loan amount.")

    # Loan Duration
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration", dur_options, format_func=lambda x: dur_display[x], help="Select loan duration.")

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        try:
            prediction = model.predict(features)
            ans = int(prediction[0])
            if ans == 0:
                st.error('According to our calculations, you will not get the loan from the bank.')
            else:
                st.success('Congratulations! You will get the loan from the bank.')
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

run()