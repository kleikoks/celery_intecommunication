from celery_config import app

from enums import Queue, AITask, BETask


@app.task(name=AITask.PRODUCE_MESSAGE.value)
def produce_message(_id: int | str):
    """Produce message to the BE service"""
    app.send_task(
        name=BETask.CONSUME_MESSAGE,
        kwargs={
            "_id": _id,
        },
        queue=Queue.BE_SERVICE
    )
    print(f"AI service: Produced message to BE service with {_id:=}")


@app.task(name=AITask.CONSUME_MESSAGE.value)
def consume_message(_id: int | str):
    """Consume message from the BE service"""
    print(f"AI service: Consumed message from BE service with {_id:=}")
    produce_message.delay(_id=_id)
