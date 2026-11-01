import json
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent

current_file = ROOT / "data/current.json"
history_file = ROOT / "data/history.json"

today = datetime.now(
    ZoneInfo("America/Sao_Paulo")
).date()

with current_file.open(encoding="utf-8") as f:
    current = json.load(f)

with history_file.open(encoding="utf-8") as f:
    history = json.load(f)

if not history:
    history.append({
        "status": current["status"],
        "start": today.isoformat(),
        "end": None
    })

else:
    last = history[-1]

    if last["status"] != current["status"]:
        last["end"] = (
            today - timedelta(days=1)
        ).isoformat()

        history.append({
            "status": current["status"],
            "start": today.isoformat(),
            "end": None
        })

with history_file.open("w", encoding="utf-8") as f:
    json.dump(history, f, indent=4, ensure_ascii=False)
    f.write("\n")
