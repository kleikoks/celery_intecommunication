from celery import Celery

app = Celery("A_tasks", broker="redis://redis:6379/0", include=("A_tasks",))
