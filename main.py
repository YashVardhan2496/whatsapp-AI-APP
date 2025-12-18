from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text

from app.core.database import async_session, engine
from app.models.reminder import Base, Reminder
from app.services.twilio_service import send_whatsapp_message

app = FastAPI(title="WhatsApp AI Reminder")

# Pydantic model for creating reminders
class ReminderCreate(BaseModel):
    message: str
    to_number: str   # e.g., +917027849920
    remind_at: datetime  # ISO format: "2025-12-19T12:30:00"

@app.on_event("startup")
async def startup():
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Schedule existing reminders in DB
    async with async_session() as session:
        result = await session.execute(
            text("SELECT * FROM reminder WHERE remind_at > :now"),
            {"now": datetime.now()}
        )
        reminders = result.fetchall()
        for r in reminders:
            delay = (r.remind_at - datetime.now()).total_seconds()
            asyncio.create_task(schedule_reminder(r.to_number, r.message, delay))

async def schedule_reminder(to_number: str, message: str, delay: float):
    if delay > 0:
        await asyncio.sleep(delay)
    send_whatsapp_message(to_number, message)
    print(f"✅ Reminder sent to {to_number}: {message}")

@app.get("/")
def root():
    return {"message": "WhatsApp AI Reminder Backend is running"}

@app.post("/reminders/")
async def create_reminder(reminder: ReminderCreate):
    # Save reminder to DB
    async with async_session() as session:
        new_reminder = Reminder(
            message=reminder.message,
            to_number=reminder.to_number,
            remind_at=reminder.remind_at
        )
        session.add(new_reminder)
        await session.commit()
        await session.refresh(new_reminder)

    # Schedule the reminder
    delay = (reminder.remind_at - datetime.now()).total_seconds()
    if delay < 0:
        # Already past, send immediately
        send_whatsapp_message(reminder.to_number, reminder.message)
        status = "sent immediately"
    else:
        asyncio.create_task(schedule_reminder(reminder.to_number, reminder.message, delay))
        status = "scheduled"

    return {
        "status": status,
        "message": reminder.message,
        "to": reminder.to_number,
        "time": reminder.remind_at
    }
