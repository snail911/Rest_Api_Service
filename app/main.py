from fastapi import FastAPI
from app.handlers import get_declared_value
from app.routes import router
from app.database import connect_to_db, disconnect_from_db, load_rates_from_json, get_current_rate
from fastapi import HTTPException

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup():
    await connect_to_db()
    await load_rates_from_json("app/rates.json")

@app.on_event("shutdown")
async def shutdown():
    await disconnect_from_db()




@app.get("/insurance-cost")
async def calculate_insurance_cost(cargo_type: str, date: str):
    try:
        current_rate = await get_current_rate(cargo_type,date)
        declared_value = get_declared_value(cargo_type)
        insurance_cost = declared_value * current_rate
        return {"insurance_cost": insurance_cost}
    except HTTPException as e:
        return {"detail": e.detail}

