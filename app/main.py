from fastapi import FastAPI, HTTPException
from app.schemas import UserSettingsCreate
from app.models import UserSettings
from app.database import load_data, save_data

app = FastAPI(
    title="Preferences API (F9)",
    description="Manage user notification settings — mute types, set quiet hours, and choose digest mode.",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Preferences API (F9) is running"}

@app.post("/settings", tags=["User Settings"])
def create_or_update_settings(settings: UserSettingsCreate):
    data = load_data()

    # Check if the user already has settings
    existing = next((item for item in data if item["user_id"] == settings.user_id), None)

    new_settings = UserSettings(
        user_id=settings.user_id,
        muted_notifications=settings.muted_notifications,
        quiet_hours_start=settings.quiet_hours_start,
        quiet_hours_end=settings.quiet_hours_end,
        digest_mode=settings.digest_mode
    )

    if existing:
        data = [item if item["user_id"] != settings.user_id else new_settings.to_dict() for item in data]
        message = "Settings updated successfully"
    else:
        data.append(new_settings.to_dict())
        message = "Settings created successfully"

    save_data(data)
    return {"status": "success", "message": message, "data": new_settings.to_dict()}

@app.get("/settings/{user_id}", tags=["User Settings"])
def get_settings(user_id: str):
    data = load_data()
    user_settings = next((item for item in data if item["user_id"] == user_id), None)

    if not user_settings:
        raise HTTPException(status_code=404, detail="User settings not found")

    return {"status": "success", "data": user_settings}
