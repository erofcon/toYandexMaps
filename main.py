from fastapi import FastAPI

from app.models.database import local_database, remote_database
from app.routes.city_name import router as city_name_router

from app.background_task.yandex_post import schedular

app = FastAPI()

app.include_router(router=city_name_router)


@app.on_event('startup')
async def startup():
    await local_database.connect()
    await remote_database.connect()
    schedular.yandex_post_start()

# @app.on_event('startup')
# async def startup():
#     await local_database.disconnect()
#     await remote_database.disconnect()
#     schedular.yandex_post_shutdown()
