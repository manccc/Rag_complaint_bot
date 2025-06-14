from fastapi import FastAPI, HTTPException
from backend.db import SessionLocal
from backend.model import Complaint
from backend.schemas import ComplaintResponse, ComplaintCreate
from backend.db import SessionLocal, init_db
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/complaints", response_model=dict)
def create_complaint(data: ComplaintCreate):
    db = SessionLocal()
    complaint_id = str(uuid4())[:8]
    complaint = Complaint(complaint_id=complaint_id, **data.dict())
    db.add(complaint)
    db.commit()
    return {"complaint_id": complaint_id, "message": "Complaint created successfully"}


@app.get("/complaints/{complaint_id}", response_model=ComplaintResponse)
def get_complaint(complaint_id: str):
    db = SessionLocal()
    complaint = db.query(Complaint).filter_by(complaint_id=complaint_id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return complaint
