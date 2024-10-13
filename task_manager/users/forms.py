from django import forms
from django.utils.translation import gettext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CreateUserForm(UserCreationForm):
    usable_password = None
    username = forms.CharField(
        label=gettext("Your Login")
    )
    first_name = forms.CharField(
        label=gettext("Your first name")
    )
    last_name = forms.CharField(
        label=gettext("Your last name")
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username']
