from tortoise import Tortoise
import json
from app.models import Rate
from fastapi import HTTPException


async def connect_to_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']},
    )
    await Tortoise.generate_schemas()


async def disconnect_from_db():
    await Tortoise.close_connections()


async def load_rates_from_json(json_file_path):
    with open(json_file_path) as file:
        rates_data = json.load(file)

    for date, rates in rates_data.items():
        for rate in rates:
            cargo_type = rate["cargo_type"]
            rate_value = float(rate["rate"])
            created_at = date
            await Rate.create(cargo_type=cargo_type, rate=rate_value, created_at=created_at)


async def get_current_rate(cargo_type: str, date: str):
    rate = await Rate.filter(
        cargo_type=cargo_type,
        created_at=date
    ).order_by('-created_at').first()

    if rate:
        return rate.rate
    else:
        raise HTTPException(status_code=404, detail="No rate found for the specified date")
