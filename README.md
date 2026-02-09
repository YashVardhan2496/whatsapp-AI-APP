📱 WhatsApp AI Reminder Assistant
A high-performance, asynchronous backend built with FastAPI and Twilio designed to schedule and deliver reminders via WhatsApp. This project features a persistent database layer and a "smart-resume" scheduler that ensures reminders are sent even if the server restarts.

🌟 Features
Asynchronous Scheduling: Built on Python’s asyncio to handle thousands of concurrent timers without performance hits.

Database Persistence: Uses SQLAlchemy (Async) and SQLite to ensure every reminder is logged and tracked.

Resilient Design: On startup, the system automatically scans the database and re-schedules any pending tasks—making it "crash-proof."

AI-Ready: Includes a pre-configured OpenAI integration layer, ready for Natural Language Processing (NLP) to handle messages like "Remind me in 2 hours."

Clean Architecture: Modular directory structure separating database models, core configuration, and external services.

🛠️ Tech Stack
Framework: FastAPI

ORM: SQLAlchemy 2.0 (Async)

Database: SQLite

Messaging: Twilio Messaging API (WhatsApp)

Environment: Pydantic Settings & Dotenv

Task Management: Python Asyncio

📂 Project Structure
Plaintext
├── app/
│   ├── api/                # API endpoint controllers
│   ├── core/
│   │   ├── config.py       # Environment variable & Secret management
│   │   └── database.py     # SQLAlchemy engine & Session setup
│   ├── models/
│   │   └── reminder.py     # SQL database schema
│   └── services/
│       ├── scheduler.py    # Async logic for message delays
│       └── twilio_service.py # Twilio API integration
├── main.py                 # App entry point & Startup lifecycle hooks
├── reminders.db            # Local SQLite database
└── .env                    # (Private) API Keys & Credentials
🚀 Getting Started
1. Installation
Bash
git clone [https://github.com/YashVardhan2496/whatsapp-AI-APP.git](https://github.com/YashVardhan2496/whatsapp-AI-APP.git)
cd whatsapp-AI-APP
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Configure Environment
Create a .env file in the root directory:

Code snippet
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_PHONE_NUMBER=+1234567890
OPENAI_API_KEY=your_openai_key
3. Launch
Bash
uvicorn main:app --reload
📡 API Reference
Create a New Reminder
POST /reminders/

Request Body:

JSON
{
  "message": "Check the oven! 🍕",
  "to_number": "+917027849920",
  "remind_at": "2026-02-15T18:30:00"
}
How it works:

Validation: The app validates the phone number and timestamp.

Storage: The reminder is saved to reminders.db.

Scheduling: An asyncio task is created to wait until the remind_at time.

Delivery: At the exact second, the twilio_service triggers a WhatsApp message.

🤖 Future Roadmap
NLP Integration: Implement a service to parse raw text messages into structured dates using the OPENAI_API_KEY.

Two-Way Interaction: Allow users to cancel or snooze reminders directly from WhatsApp.

Timezone Support: Automatically adjust reminders based on the user's local time.

Developed by Yash Vardhan License: MIT
