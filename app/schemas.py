from pydantic import BaseModel, Field
from typing import List, Optional

class UserSettingsCreate(BaseModel):
    user_id: str = Field(..., example="user123")
    muted_notifications: Optional[List[str]] = Field(default=[], example=["marketing", "system_alerts"])
    quiet_hours_start: Optional[str] = Field(default="22:00", example="22:00")  # 24-hour format
    quiet_hours_end: Optional[str] = Field(default="07:00", example="07:00")
    digest_mode: Optional[bool] = Field(default=False, example=True)
