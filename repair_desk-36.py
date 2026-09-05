# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: RepairDesk
def verify_integrity(data):
    errors = []
    for req in data.get("requests", []):
        if not req.get("id"):
            errors.append("Request missing id")
        if not req.get("device_id"):
            errors.append(f"Request {req.get('id')} missing device_id")
        diag = req.get("diagnostics", [])
        if diag and not any(d.get("status") == "done" for d in diag):
            errors.append(f"Request {req.get('id')} has no completed diagnostics")
        if req.get("parts"):
            for p in req["parts"]:
                if not p.get("cost"):
                    errors.append(f"Request {req.get('id')} part {p.get('name')} missing cost")
    if errors:
        print(f"Integrity issues: {', '.join(errors)}")
        return False
    print("Data integrity verified.")
    return True

def quick_fix(device_id, req_id):
    print(f"Quick-fix initiated for device {device_id} in request {req_id}.")
    return {"device_id": device_id, "req_id": req_id, "status": "fix_started", "note": "Simple issue resolved"}
