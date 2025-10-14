
---

### 📁 **3️⃣ F9_README.md** (Preferences API)

```markdown
# ⚙️ F9 – Preferences API (User Settings)

## 📘 Overview
This API lets users control notification preferences:  
- Mute notification types  
- Define **quiet hours** (Do Not Disturb)  
- Enable **digest mode** for grouped updates  

Settings are stored **per user** in JSON format.

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate


2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run FastAPI
uvicorn app.main:app --reload

🌐 Swagger URL

Open:
👉 http://127.0.0.1:8000/docs

You’ll see the F9 – Preferences API section.

🧪 Example Request (POST /f9/settings)
{
  "user_id": "user123",
  "muted_notifications": ["marketing", "system_alerts"],
  "quiet_hours_start": "22:00",
  "quiet_hours_end": "07:00",
  "digest_mode": true
}

✅ Expected Response
{
  "status": "success",
  "message": "Settings created successfully",
  "data": {
    "user_id": "user123",
    "muted_notifications": ["marketing", "system_alerts"],
    "quiet_hours_start": "22:00",
    "quiet_hours_end": "07:00",
    "digest_mode": true,
    "updated_at": "2025-10-07T22:50:00"
  }
}

📁 Output Storage

User preferences are stored in:

data/user_settings.json

✅ Swagger Test Success

Once Swagger shows:

"status": "success"


✅ Your F9 Preferences API has successfully stored user settings.

