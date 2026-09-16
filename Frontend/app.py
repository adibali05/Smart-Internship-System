import streamlit as st
import requests
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Smart Internship Dashboard", layout="wide")

# Backend API URL
API_URL = "http://127.0.0.1:8000"

st.title("🎓 Smart Internship Monitoring System")
st.markdown("---")

# ---------------- SIDEBAR: Student Portal (Log Submission) ---------------- #
st.sidebar.header("📝 Student Portal")
st.sidebar.markdown("Submit your weekly log for AI evaluation.")

student_id = st.sidebar.text_input("Student ID (e.g., STU001)")
log_text = st.sidebar.text_area("What did you work on this week?", height=150)

if st.sidebar.button("Submit Log (AI Evaluate)"):
    if student_id and log_text:
        with st.sidebar.status("AI is analyzing your log..."):
            # Sending data to the CORRECT backend link
            response = requests.post(f"{API_URL}/submit-log/", json={"student_id": student_id, "log_text": log_text})
            
        if response.status_code == 200:
            st.sidebar.success("✅ Log submitted and scored by AI!")
            st.sidebar.json(response.json()["score"])
        else:
            st.sidebar.error("❌ Error submitting log.")
    else:
        st.sidebar.warning("⚠️ Please fill both fields.")

# ---------------- MAIN PAGE: Admin Dashboard ---------------- #
st.subheader("📊 Admin / University Dashboard")

try:
    # Fetching data from the CORRECT backend link
    response = requests.get(f"{API_URL}/dashboard-data/")
    if response.status_code == 200:
        data = response.json()
        logs = data.get("logs", [])
        
        if logs:
            # Convert JSON data to a beautiful Pandas DataFrame table
            df = pd.DataFrame(logs)
            st.dataframe(df, use_container_width=True)
            
            # Show a chart to impress evaluators
            st.subheader("📈 AI Technical Scores Overview")
            st.bar_chart(df.set_index("student_id")["technical_score"])
        else:
            st.info("No logs submitted yet. Use the sidebar to submit a test log!")
    else:
        st.error("Could not fetch data from backend.")
except Exception as e:
    st.error(f"Backend is not running. Please start the FastAPI server. Error: {e}")