import django_filters as filter
from tasks.models import Task

class TaskFilter(filter.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'executor', 'label']