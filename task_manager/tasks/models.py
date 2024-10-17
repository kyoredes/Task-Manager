from django.db import models
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='author',
    )
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='executor',
    )
    label = models.ManyToManyField(
        Label,
        related_name='tasks',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name