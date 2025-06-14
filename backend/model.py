from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    complaint_id = Column(String, unique=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    complaint_details = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
