from app.models.database import local_database
from app.models import route as route_model
from app.schemas import route as route_schemas


async def create_route(route: route_schemas.RouteCreate) -> bool:
    query = route_model.route.insert().values(
        route=route.route,
        city_id=route.city_id
    )

    try:
        return await local_database.execute(query=query)
    except Exception:
        return False
