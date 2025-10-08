from datetime import datetime

class UserSettings:
    def __init__(self, user_id: str, muted_notifications: list, quiet_hours_start: str, quiet_hours_end: str, digest_mode: bool):
        self.user_id = user_id
        self.muted_notifications = muted_notifications
        self.quiet_hours_start = quiet_hours_start
        self.quiet_hours_end = quiet_hours_end
        self.digest_mode = digest_mode
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "muted_notifications": self.muted_notifications,
            "quiet_hours_start": self.quiet_hours_start,
            "quiet_hours_end": self.quiet_hours_end,
            "digest_mode": self.digest_mode,
            "updated_at": self.updated_at
        }
