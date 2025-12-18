from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class Reminder(Base):
    __tablename__ = "reminder"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    to_number = Column(String, nullable=False)
    remind_at = Column(DateTime, nullable=False)
