from django import forms
from django.utils.translation import gettext
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    usable_password = None
    username = forms.CharField(
        label = gettext("Your Login")
    )
    first_name = forms.CharField(
        label = gettext("Your first name")
    )
    last_name = forms.CharField(
        label = gettext("Your last name")
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

# class UsersLoginForm(forms.Form):
#     login = forms.CharField(
#         label = gettext("Login")
#     )
#     psswd = forms.CharField(
#         label = gettext("Password")
#     )