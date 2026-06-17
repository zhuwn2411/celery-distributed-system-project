from celery import Celery
import time
import random

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task(bind=True)
def add(self, x, y):

    processing_time = random.randint(2, 5)

    print(
        f"Worker xử lý task {self.request.id} "
        f"({x}+{y}) trong {processing_time}s"
    )

    time.sleep(processing_time)

    return x + y