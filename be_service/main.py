import random
import time

from celery_config import app
from enums import Queue, BETask


if __name__ == '__main__':
    while True:
        _id = random.randint(0, 1000)
        print(f"Runner: {_id:=}")
        app.send_task(
            name=BETask.PRODUCE_MESSAGE,
            kwargs={
                "_id": _id,
            },
            queue=Queue.BE_SERVICE
        )
        time.sleep(15)
