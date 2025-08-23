from A_celery import app


@app.task(queue="B", name="produce_to_b")
def produce_to_b(some_id: int | str):
    pass


@app.task(name="produce_to_a")
def consume_what_b_returned(some_id: int | str):
    print(f"Consumed what B produced back ({some_id})")
