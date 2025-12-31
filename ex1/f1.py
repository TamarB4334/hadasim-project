from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()
DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

class Payload(BaseModel):
    name: str
    message: str

@app.post("/save")
def save_payload(payload: Payload):
    with open(DATA_FILE, "r+") as f:
        data = json.load(f)
        data.append(payload.dict())
        f.seek(0)
        json.dump(data, f)
    return {"status": "saved", "payload": payload}

@app.get("/last")
def get_last_payloads():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return {"last_10": data[-10:]}