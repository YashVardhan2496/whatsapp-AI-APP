# app/services/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.services.twilio_service import send_whatsapp_message

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")


def schedule_whatsapp_reminder(run_at: datetime, to_number: str, message: str):
    scheduler.add_job(
        send_whatsapp_message,
        trigger="date",
        run_date=run_at,
        args=[to_number, message],
        id=f"{to_number}-{run_at.timestamp()}",
        replace_existing=True,
    )
