from django.db import models
from statuses.models import Status
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author')
    executor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='customer')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title