from django import forms
from task_manager.statuses.models import Status
from django.utils.translation import gettext as translate


class StatusCreateForm(forms.ModelForm):
    title = forms.CharField(label=translate("Name"))

    class Meta:
        model = Status
        fields = ['title']
