# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: RepairDesk
SELECTED = []

def toggle_favorite(rec):
    if rec in SELECTED:
        SELECTED.remove(rec)
    else:
        SELECTED.append(rec)

def save_selected():
    try:
        with open("favorites.json", "w", encoding="utf-8") as f:
            json.dump([r.get("id") for r in SELECTED], f)
    except Exception:
        pass

def load_selected():
    try:
        with open("favorites.json", "r", encoding="utf-8") as f:
            return [r for r in SELECTED if r.get("id") in json.load(f)]
    except Exception:
        return []

def print_selected():
    if not SELECTED:
        print("Избранное пусто. Добавьте записи через toggle_favorite().")
        return
    print("=== Избранные записи ===")
    for r in SELECTED:
        print(f"- {r}")

print_selected()
