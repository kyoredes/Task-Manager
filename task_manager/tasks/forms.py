from django import forms
from django.utils.translation import gettext as translate
from django.contrib.auth import get_user_model
from tasks.models import Task
from statuses.models import Status


class TaskCreateForm(forms.ModelForm):
    title = forms.CharField(label=translate("Name"))
    description = forms.CharField(label=translate("Description"))
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    executor = forms.ModelChoiceField(queryset=get_user_model().objects.all())
    # tags =
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'executor']
