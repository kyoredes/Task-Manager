import django_filters as filter
from tasks.models import Task
from django.utils.translation import gettext as translate
from django import forms


class TaskFilter(filter.FilterSet):
    user_filter = filter.BooleanFilter(
        label=translate('show only my tasks'),
        widget=forms.CheckboxInput(),
        method='filter_by_user',
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
