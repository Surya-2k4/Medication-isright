import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medication Validation System", layout="centered")

st.title("🩺 Patient Medication Validation")
st.write("Upload a CSV file to verify whether prescribed medications are correct for the disease.")

# Disease → Correct Medication Mapping
DISEASE_MEDICATION_MAP = {
    "Diabetes": ["Metformin", "Insulin"],
    "Malaria": ["Chloroquine", "Artemisinin"],
    "Hypertension": ["Amlodipine", "Losartan"],
    "Fever": ["Paracetamol", "Ibuprofen"]
}

uploaded_file = st.file_uploader("Upload Patient CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Data")
    st.dataframe(df)

    def check_medication(row):
        disease = str(row["Disease"]).strip()
        medication = str(row["Medication"]).strip()

        if disease in DISEASE_MEDICATION_MAP:
            if medication in DISEASE_MEDICATION_MAP[disease]:
                return "Correct"
            else:
                return "Incorrect"
        else:
            return "Unknown Disease"

    if st.button("Validate Medications"):
        df["Medication_Status"] = df.apply(check_medication, axis=1)

        st.subheader("✅ Validation Results")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Updated CSV",
            data=csv,
            file_name="patients_validated.csv",
            mime="text/csv"
        )
