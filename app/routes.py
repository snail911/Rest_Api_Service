from fastapi import APIRouter, HTTPException

from app.models import Rate

router = APIRouter()


@router.get("/rates/{cargo_type}")
async def get_rate(cargo_type: str):
    rate = await Rate.filter(cargo_type=cargo_type).order_by('-created_at').first()
    if rate:
        return {"rate": rate.rate}
    else:
        return {"rate": None}

@router.post("/rates")
async def create_rate(cargo_type: str, rate: float):
    try:
        new_rate = await Rate.create(cargo_type=cargo_type, rate=rate)
        return {"id": new_rate.id, "cargo_type": new_rate.cargo_type, "rate": new_rate.rate}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/rates/{rate_id}")
async def update_rate(rate_id: int, rate: float):
    try:
        existing_rate = await Rate.get_or_none(id=rate_id)
        if existing_rate:
            existing_rate.rate = rate
            await existing_rate.save()
            return {"id": existing_rate.id, "cargo_type": existing_rate.cargo_type, "rate": existing_rate.rate}
        else:
            raise HTTPException(status_code=404, detail="Rate not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/rates/{rate_id}")
async def delete_rate(rate_id: int):
    try:
        existing_rate = await Rate.get_or_none(id=rate_id)
        if existing_rate:
            await existing_rate.delete()
            return {"message": "Rate deleted"}
        else:
            raise HTTPException(status_code=404, detail="Rate not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))