from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from backend.database import students_collection, logs_collection, init_db
from backend.ai_scorer import score_log_text # (Yeh pichli file waisi hi rahegi)

app = FastAPI(title="Smart Internship API")

class LogCreate(BaseModel):
    student_id: str
    log_text: str

@app.on_event("startup")
def startup_db():
    init_db()

@app.post("/submit-log/")
def submit_log(log: LogCreate):
    # AI se log ka score nikalein
    ai_result = score_log_text(log.log_text)
    
    # MongoDB mein document save karne ke liye dictionary banayein
    log_document = {
        "student_id": log.student_id,
        "log_text": log.log_text,
        "technical_score": ai_result["technical_score"],
        "soft_skills_score": ai_result["soft_skills_score"],
        "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    logs_collection.insert_one(log_document)
    
    return {"message": "Log successfully analyzed and saved to MongoDB!", "score": ai_result}

@app.get("/dashboard-data/")
def get_dashboard_data():
    # MongoDB se saara data fetch karein (_id field ko exclude karke kyunki wo JSON serializable nahi hota)
    students = list(students_collection.find({}, {"_id": 0}))
    logs = list(logs_collection.find({}, {"_id": 0}))
    return {"students": students, "logs": logs}