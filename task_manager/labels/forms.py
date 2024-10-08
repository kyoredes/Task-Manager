from django import forms
from task_manager.labels.models import Label
from django.utils.translation import gettext as translate


class LabelCreateForm(forms.ModelForm):
    name = forms.CharField(label=translate('Name'))

    class Meta:
        model = Label
        fields = ['name']
