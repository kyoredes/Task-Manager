from django import forms
from statuses.models import Status
from django.utils.translation import gettext as translate

class StatuseCreateForm(forms.ModelForm):
    title = forms.CharField(label=translate("Name"))
    class Meta:
        model = Status
        fields = ['title']