# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: RepairDesk
def dry_run_mode(active: bool = False):
    """Toggle dry-run mode. When active, write operations are logged instead of executed."""
    global _dry_run
    _dry_run = active
    if active:
        print("[DRY-RUN] All write operations will be simulated.")
    else:
        print("[NORMAL] Operations will be executed normally.")
