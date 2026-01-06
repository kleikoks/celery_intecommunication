from celery import Celery

from enums import Queue

app = Celery(broker="redis://redis:6379/0", include=("tasks",))

# This controls publishing, not consuming
# .delay() depending on the task name will go to corresponding queue
app.conf.task_routes = {
    f"be.*": Queue.BE_SERVICE,
    f"ai.*": Queue.AI_SERVICE,
}
