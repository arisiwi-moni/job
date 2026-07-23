# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: RepairDesk
def add_reminders():
    """Простая система напоминаний с датой выполнения."""
    import datetime

    def create_reminder(description, due_date):
        reminder = {
            "description": description,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        return reminder

    def mark_reminder_complete(reminder_id):
        for i, r in enumerate(reminders):
            if r["id"] == reminder_id:
                reminders[i]["completed"] = True
                break
        else:
            raise ValueError(f"Напоминание с ID {reminder_id} не найдено")

    def get_due_reminders():
        today = datetime.date.today()
        return [r for r in reminders if not r["completed"] and r["due_date"].date() == today]

    reminders = []
