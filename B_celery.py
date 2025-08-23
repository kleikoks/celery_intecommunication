from celery import Celery

app = Celery("B_tasks", broker="redis://redis:6379/0", include=("B_tasks",))
