# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: RepairDesk
def archive_records(records, days_old=365, status_done='done'):
    import time
    cutoff = time.time() - days_old * 86400
    archived = []
    for r in records:
        if r.get('status') == status_done and (r.get('created_at', 0) < cutoff or r.get('updated_at', 0) < cutoff):
            r['status'] = 'archived'
            r['archived_at'] = int(time.time())
            archived.append(r)
    return records, archived
