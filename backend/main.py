from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.database import init_db, logs_collection
from backend.ai_scorer import score_log_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LogEntry(BaseModel):
    student_id: str
    log_text: str

@app.on_event("startup")
def startup_db():
    init_db()

@app.post("/submit-log/")
async def submit_log(entry: LogEntry):
    try:
        score = score_log_text(entry.log_text)
        
        log_data = {
            "student_id": entry.student_id,
            "log_text": entry.log_text,
            "technical_score": score.get("technical_score", 0),
            "soft_skills_score": score.get("soft_skills_score", 0)
        }
        logs_collection.insert_one(log_data)
        
        return {"message": "Log submitted successfully", "score": score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/dashboard-data/")
async def get_dashboard_data():
    try:
        logs = list(logs_collection.find({}, {"_id": 0}))
        return {"logs": logs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    