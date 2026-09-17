# 🎓 Smart Internship Management & Monitoring System

An AI-powered, single-platform solution designed to help institutions digitally monitor, evaluate, and manage the complete internship lifecycle of students using Natural Language Processing (NLP).

## 🚀 Key Features
* **AI-Powered Log Evaluation:** Automatically scores weekly student text logs for technical depth and soft skills using HuggingFace NLP models.
* **Animated Real-time Dashboard:** Interactive, sleek Dark Mode UI built with Tailwind CSS and Chart.js for instant analytics.
* **Seamless REST API:** Fully asynchronous backend built with FastAPI (CORS enabled for cross-origin requests).
* **Cloud Database:** Flexible NoSQL data storage handling unstructured logs efficiently.

## 🛠️ Tech Stack
* **Frontend:** Custom HTML5, Tailwind CSS, Chart.js, Vanilla JS
* **Backend:** FastAPI, Uvicorn
* **Database:** MongoDB Atlas (Cloud NoSQL)
* **AI/NLP Engine:** HuggingFace `transformers` (Zero-shot classification pipeline)

## ⚙️ How to Run Locally

**1. Clone the repository and install dependencies:**
```bash
git clone [https://github.com/adibali05/Smart-Internship-System.git](https://github.com/adibali05/Smart-Internship-System.git)
cd Smart-Internship-System
pip install -r requirements.txt