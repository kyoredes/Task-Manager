from django import forms

class LabelCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
