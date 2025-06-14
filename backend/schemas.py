from pydantic import BaseModel, EmailStr

class ComplaintCreate(BaseModel):
    name: str
    phone_number: str
    email: EmailStr
    complaint_details: str

from datetime import datetime

class ComplaintResponse(BaseModel):
    complaint_id: str
    name: str
    phone_number: str
    email: str
    complaint_details: str
    created_at: datetime
