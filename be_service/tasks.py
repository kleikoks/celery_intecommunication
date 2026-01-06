from celery_config import app
from enums import Queue, BETask, AITask


@app.task(name=BETask.PRODUCE_MESSAGE)
def produce_message(_id: int | str):
    """Produce message to the AI service"""
    app.send_task(
        name=AITask.CONSUME_MESSAGE,
        kwargs={
            "_id": _id,
        },
        queue=Queue.AI_SERVICE
    )
    print(f"BE service: Produced message to AI service with {_id:=}")


@app.task(name=BETask.CONSUME_MESSAGE)
def consume_message(_id: int | str):
    """Consume message from AI service"""
    print(f"BE service: consumed message from AI service with {_id:=}")
