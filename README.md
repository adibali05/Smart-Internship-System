🎓 Smart Internship Management & Monitoring System

An AI-powered Minimum Viable Product (MVP) designed to help institutions digitally monitor and manage the internship lifecycle of their students. This platform uses Natural Language Processing (NLP) to evaluate weekly student logs and provides a real-time dashboard for university administrators.

🚀 Key Features

AI Log Scoring: Uses Hugging Face Zero-Shot Classification to evaluate student logs based on technical depth and problem-solving.

Student Portal: A simple interface for students to select their profile and submit weekly progress logs.

Admin Dashboard: A real-time tracker for university staff to monitor which students are excelling and which need intervention (Red Flag system).

Automated Feedback: Generates instant AI feedback for students upon log submission.

🛠️ Tech Stack

Backend: FastAPI (Python)

Frontend: Streamlit

AI/NLP Engine: Hugging Face transformers (DistilBART)

Database: SQLite & SQLAlchemy

💻 How to Run Locally

1. Setup Virtual Environment

python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate


2. Install Dependencies

pip install -r requirements.txt


3. Start the Backend API (FastAPI)

Run this command in your terminal. It will start the API server on http://127.0.0.1:8000.

uvicorn backend.main:app --reload


Note: The first time you run this, it will download the Hugging Face AI model (approx 1.5 GB). Please be patient.

4. Start the Frontend Dashboard (Streamlit)

Open a new terminal tab, activate the environment again, and run:

streamlit run frontend/app.py


This will automatically open the dashboard in your web browser.

📌 Future Scope

Integration of Geo-fenced mobile attendance tracking.

Automated tripartite agreement generation via digital signatures.

Matching algorithm to connect students with employer job postings.