from fastapi import FastAPI, HTTPException
from my_env import EmergencyEnv, Action
import uvicorn

app = FastAPI()
sim = EmergencyEnv()

@app.get("/status")
def get_status():
    is_done = sim.steps_taken >= 100 or sim.sector_integrity <= 0
    return {
        "budget": int(sim.budget), "lives_saved": int(sim.lives_saved),
        "steps_taken": int(sim.steps_taken), "integrity": float(sim.sector_integrity),
        "incidents": [{"id": i.id, "type": i.type, "x": i.x, "y": i.y, "severity": i.severity, "p_score": sim.get_priority_score(i)} for i in sim.incidents],
        "districts": sim.districts, "unit_levels": sim.unit_levels, "unit_xp": sim.unit_xp,
        "is_done": is_done, "recovery_types": sim.recovery_types, "history": sim.history, 
        "unit_ready": sim.unit_ready, "cooldowns": sim.cooldowns, "fleet_usage": sim.fleet_usage
    }

@app.post("/reset")
def reset():
    sim.reset(); return {"ok": True}

@app.post("/dispatch")
def dispatch(action: Action):
    sim.step(action); return {"ok": True}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)