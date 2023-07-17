from app.models.database import database
from app.models import vehicle_type as vehicle_type_model
from app.schemas import vehicle_type as vehicle_type_schemas


async def create_vehicle_type(vehicle_type: vehicle_type_schemas.VehicleTypeCreate) -> bool:
    query = vehicle_type_model.vehicle_type.insert().values(
        vehicle_type=vehicle_type.vehicle_type

    )

    try:
        return await database.execute(query=query)
    except Exception:
        return False
