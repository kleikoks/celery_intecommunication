from A_celery import app


@app.task(name="produce_to_a", queue="A")
def forward_back_to_a(some_id: int | str):
    pass


@app.task(name="produce_to_b")
def consume_from_a(some_id: int | str):
    print(f"Consumed by B: {some_id}")
    forward_back_to_a.delay(some_id=some_id)
    print(f"Forwarded back to A: {some_id}")
