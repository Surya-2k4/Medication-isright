# 🩺 Patient Medication Validation System

A simple **Streamlit-based web application** that validates whether the prescribed medication for a patient is **correct or incorrect** based on the diagnosed disease.  
The system processes patient data from a CSV file and appends a validation status for each record.

---

## 📌 Project Overview

In healthcare data management, verifying whether a medication aligns with a diagnosed disease is critical.  
This project provides a **rule-based validation system** that:

- Accepts patient data in CSV format
- Checks disease–medication correctness
- Appends a validation status
- Allows users to download the updated dataset

This application is designed for **educational, academic, and prototype purposes**.

---

## ⚙️ How It Works

1. User uploads a CSV file containing patient records  
2. The app reads the file and extracts:
   - Disease
   - Medication
3. A predefined **disease → allowed medications mapping** is applied
4. Each record is validated:
   - ✅ Correct
   - ❌ Incorrect
   - ⚠️ Unknown Disease
5. A new column `Medication_Status` is added
6. The updated CSV can be downloaded

---

## 📄 Expected CSV Columns

Minimum required columns:
- `Disease`
- `Medication`

Sample dataset can include additional metadata such as:
- Patient name
- Age
- Doctor
- Hospital
- Visit date

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**

---

## 🚀 How to Run Locally

```bash
pip install streamlit pandas
streamlit run app.py
