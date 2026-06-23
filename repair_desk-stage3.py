# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: RepairDesk
class RepairDesk:
    def __init__(self):
        self.requests = []
        self.devices = {}
        self.diagnostics = {}
        self.parts = {}

    def add_request(self, req_id, device_name, status="new"):
        if not device_name in self.devices:
            self.devices[device_name] = {"model": "Unknown", "serial": None}
        
        request = {
            "id": req_id,
            "device": device_name,
            "status": status,
            "diagnosis": "",
            "cost": 0.0,
            "parts_used": []
        }
        self.requests.append(request)
        return request

    def add_diagnosis(self, req_id, diagnosis_text):
        for req in self.requests:
            if req["id"] == req_id:
                req["diagnosis"] = diagnosis_text
                break

    def add_parts_cost(self, req_id, part_name, cost):
        total_cost = 0.0
        parts_list = []
        
        for req in self.requests:
            if req["id"] == req_id:
                current_total = req.get("cost", 0.0) + cost
                req["cost"] = current_total
                parts_list.append({"name": part_name, "price": cost})
                break
        
        return total_cost

    def get_request(self, req_id):
        for req in self.requests:
            if req["id"] == req_id:
                return req
        return None
