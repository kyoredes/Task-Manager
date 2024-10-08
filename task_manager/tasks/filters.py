import django_filters as filter
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as translate
from django import forms


class TaskFilter(filter.FilterSet):
    user_filter = filter.BooleanFilter(
        label=translate('show only my tasks'),
        widget=forms.CheckboxInput(),
        method='filter_by_user',
    )
    status = filter.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=translate('Status'),
    )
    executor = filter.ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        label=translate('Executor'),
    )
    label = filter.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=translate('Label')
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.get('request', None)
        super().__init__(*args, **kwargs)

    def filter_by_user(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
