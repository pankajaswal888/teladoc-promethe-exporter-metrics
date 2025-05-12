from prometheus_client import Gauge
from .models import Task

class TaskExporter:
    def __init__(self):
        self.task_duration = Gauge(
            'task_duration',
            'Duration of tasks in seconds',
            ['tool', 'task', 'status']
        )

    def process_task(self, task):
        self.task_duration.labels(
            tool=task.tool,
            task=task.task,
            status=task.status.value
        ).set(task.duration)
