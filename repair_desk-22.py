# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: RepairDesk
def check_overdue_reminders(self):
        """Проверяет просроченные напоминания для заявок."""
        now = datetime.now()
        overdue = []
        for ticket in self.tickets:
            if hasattr(ticket, 'reminder_date') and hasattr(ticket, 'status'):
                if isinstance(ticket.reminder_date, datetime) and \
                   (ticket.status not in ('closed', 'cancelled')) and \
                   now > ticket.reminder_date:
                    overdue.append(ticket)
        return overdue
