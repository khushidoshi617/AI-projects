import streamlit as st

st.set_page_config(
    page_title="Diabetes Risk Assessment",
    page_icon="🩺"
)

st.title("🩺 Diabetes Risk Assessment")

st.write(
    "Enter some basic health information to see a "
    "simple educational risk assessment."
)

st.info(
    "This application is for educational purposes only. "
    "It does not diagnose diabetes or replace medical advice."
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=25
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=22.0,
    step=0.1
)

glucose = st.number_input(
    "Glucose Level",
    min_value=50,
    max_value=300,
    value=100
)

family_history = st.selectbox(
    "Family history of diabetes?",
    ["No", "Yes"]
)

physical_activity = st.selectbox(
    "Regular physical activity?",
    ["Yes", "No"]
)

if st.button("Assess Risk"):

    score = 0

    if age >= 45:
        score += 1

    if bmi >= 25:
        score += 1

    if glucose >= 126:
        score += 2
    elif glucose >= 100:
        score += 1

    if family_history == "Yes":
        score += 1

    if physical_activity == "No":
        score += 1

    st.subheader("Assessment Result")

    if score <= 1:
        st.success("Lower risk indicators")
    elif score <= 3:
        st.warning("Some risk indicators detected")
    else:
        st.error("Several risk indicators detected")

    st.write(
        "This result is only an educational demonstration. "
        "A healthcare professional and appropriate medical "
        "testing are required for actual assessment."
    )
