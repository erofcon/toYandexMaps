from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .yandex_crud import yandex_crud_task


class YandexPost:
    scheduler = AsyncIOScheduler()

    def yandex_post_start(self):
        self.scheduler.add_job(yandex_crud_task, trigger='interval', seconds=20)
        self.scheduler.start()
        # self.scheduler.add_job(foton_request_task, trigger='interval', minutes=5)
        # self.scheduler.add_listener(scheduler_listener)
        # self.scheduler.start()

    def yandex_post_shutdown(self):
        self.scheduler.shutdown()

    def yandex_post_pause(self):
        self.scheduler.pause()

    def yandex_post_resume(self):
        self.scheduler.resume()

    def yandex_post_status(self):
        return self.scheduler.state


schedular = YandexPost()
