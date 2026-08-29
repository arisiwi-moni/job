# === Stage 32: Добавь журнал действий пользователя ===
# Project: RepairDesk
import json

class ActionLog:
    def __init__(self):
        self.entries = []
        self._load()

    def _load(self):
        try:
            with open("repair_log.json", "r", encoding="utf-8") as f:
                self.entries = json.load(f)
        except FileNotFoundError:
            self.entries = []

    def add(self, user, action, details=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "action": action,
            "details": details or ""
        }
        self.entries.append(entry)
        self._save()

    def _save(self):
        with open("repair_log.json", "w", encoding="utf-8") as f:
            json.dump(self.entries, f, indent=2, ensure_ascii=False)

    def get_log(self):
        return self.entries[-50:]

    def clear(self):
        self.entries = []
        self._save()

log = ActionLog()
