📱 WhatsApp AI Reminder Assistant

A high-performance, asynchronous backend built with FastAPI and Twilio to schedule and deliver reminders via WhatsApp.
Includes a persistent database layer and a smart-resume scheduler that guarantees delivery even after server restarts.

🌟 Features

• Asynchronous Scheduling
Built on Python asyncio to handle thousands of concurrent timers efficiently.

• Database Persistence
Uses SQLAlchemy 2.0 (Async) with SQLite to log and track every reminder.

• Resilient Design
On startup, the system scans the database and re-schedules all pending reminders — making it crash-proof.

• AI-Ready
Pre-configured OpenAI integration layer for NLP commands like
“Remind me in 2 hours”.

• Clean Architecture
Modular structure separating APIs, core config, models, and services.

🛠️ Tech Stack

• Framework: FastAPI
• ORM: SQLAlchemy 2.0 (Async)
• Database: SQLite
• Messaging: Twilio Messaging API (WhatsApp)
• Environment: Pydantic Settings & Dotenv
• Task Management: Python Asyncio

📂 Project Structure

├── app/
│   ├── api/                  # API endpoint controllers
│   ├── core/
│   │   ├── config.py         # Environment variables & secrets
│   │   └── database.py       # SQLAlchemy engine & session setup
│   ├── models/
│   │   └── reminder.py       # Database schema
│   └── services/
│       ├── scheduler.py      # Async reminder scheduling
│       └── twilio_service.py # Twilio WhatsApp integration
│
├── main.py                   # App entry point & startup hooks
├── reminders.db              # Local SQLite database
└── .env                      # Private credentials


🚀 Getting Started

🔹 1. Installation

git clone https://github.com/YashVardhan2496/whatsapp-AI-APP.git
cd whatsapp-AI-APP
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt


🔹 2. Configure Environment

Create a .env file in the root directory:

TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_PHONE_NUMBER=+1234567890
OPENAI_API_KEY=your_openai_key


⚠️ Never commit .env to version control.

🔹 3. Launch the App

uvicorn main:app --reload


Server runs at:

http://127.0.0.1:8000


📡 API Reference

🧾 Create a New Reminder

POST /reminders/

Request Body:

{
  "message": "Check the oven! 🍕",
  "to_number": "+917027849920",
  "remind_at": "2026-02-15T18:30:00"
}


How it works:

• Validation → phone number & timestamp checked
• Storage → reminder saved to reminders.db
• Scheduling → asyncio task created
• Delivery → WhatsApp message sent at exact second

🤖 Future Roadmap

• NLP parsing for natural language reminders
• Two-way WhatsApp interaction (cancel / snooze)
• Automatic timezone detection & adjustment

👨‍💻 Developed by: Yash Vardhan
📄 License: MIT

🔥 Why this works on WhatsApp

No Markdown-dependent headings

All trees & code in monospace blocks

Emojis used as visual separators

Zero indentation loss

If you want, I can also:

Optimize this for GitHub README

Make a LinkedIn project post

Convert it into portfolio documentation

Just say the move 🚀
