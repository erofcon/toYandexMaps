import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.models.database import local_database, remote_database
from app.routes.city_name import router as city_name_router
from app.routes.vehicle_type import router as vehicle_type_router
from app.routes.route import router as route_router
from app.routes.transport import router as transport_router

from app.background_task.yandex_post import schedular

app = FastAPI()

app.include_router(router=city_name_router)
app.include_router(router=vehicle_type_router)
app.include_router(router=route_router)
app.include_router(router=transport_router)

logger.add("logs/log.log", rotation="00:00")


@app.on_event('startup')
async def startup():
    await local_database.connect()
    await remote_database.connect()
    schedular.yandex_post_start()


@app.on_event('shutdown')
async def shutdown():
    await local_database.disconnect()
    await remote_database.disconnect()
    schedular.yandex_post_shutdown()


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='0.0.0.0'
    )
