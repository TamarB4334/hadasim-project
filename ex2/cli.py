import typer
from pydantic import BaseModel, ValidationError
import json
from pathlib import Path

app = typer.Typer()
DATA_FILE = Path("data.jsonl")

class Payload(BaseModel):
    name: str
    message: str

@app.command()
def append(payload: str = typer.Option(...)):
    
    try:

        parts = payload.split(",")
        data = {}
        for part in parts:
            key, value = part.split("=")
            data[key.strip()] = value.strip()

        obj = Payload.parse_obj(data)

        with open(DATA_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(obj.dict(), ensure_ascii=False) + "\n")

        print("נשמר:", obj)

    except (ValueError, ValidationError):
        print(" הקלט לא תקין. השתמשי בפורמט: name=...,message=...")

@app.command()
def tail():
    if not DATA_FILE.exists():
        print("אין עדיין נתונים בקובץ.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    last_items = lines[-10:]
    for line in last_items:
        try:
            obj = Payload.parse_obj(json.loads(line))
            print(f"- {obj.name}: {obj.message}")
        except ValidationError:
            print(" שורה לא תקינה בקובץ")

if __name__ == "__main__":
    app()