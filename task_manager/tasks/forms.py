from django import forms
from django.utils.translation import gettext as translate
from django.contrib.auth import get_user_model
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskCreateForm(forms.ModelForm):
    name = forms.CharField(label=translate("Name"))
    description = forms.CharField(
        label=translate("Description"),
        widget=forms.Textarea(),
        required=False,
    )
    status = forms.ModelChoiceField(
        label=translate('Status'),
        queryset=Status.objects.all(),
    )
    executor = forms.ModelChoiceField(
        label=translate('Executor'),
        queryset=get_user_model().objects.all(),
        required=False,
    )
    labels = forms.ModelMultipleChoiceField(
        label=translate('Labels'),
        queryset=Label.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
