from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as translate
from utils.utils_classes import CustomLoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models.functions import Concat
from django.db.models import Value


class UserListView(ListView):
    model = get_user_model()
    template_name = 'table.html'
    context_object_name = 'info'
    paginate_by = 20
    tables = [
        translate('ID'),
        translate('Useraname'),
        translate('Full name'),
        translate('Created at'),
    ]
    extra_context = {
        'title': 'Users',
        'tables': tables,
        'url_name_change': 'update_user',
        'url_name_delete': 'delete_user',
        'button_value': translate('Create user'),
        'button_url': reverse_lazy('create_user'),
    }

    def get_queryset(self):
        return self.model.objects.annotate(
            full_name=Concat(
                'first_name', Value(' '), 'last_name'
            )
        ).values('id', 'username', 'full_name', 'date_joined')


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = CreateUserForm
    template_name = 'forms.html'
    success_url = reverse_lazy('home')
    success_message = translate("User registered successfully")
    extra_context = {
        'title': translate('Create User'),
        'button': translate('Create'),
    }


class UserUpdateView(
    UserPassesTestMixin,
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = User
    form_class = CreateUserForm
    # fields = ['username', 'first_name', 'last_name', 'password']
    template_name = 'forms.html'
    success_url = reverse_lazy('home')
    success_message = translate("User successfully changed")
    extra_context = {
        'title': translate('Update user'),
        'button': translate('Update'),
    }

    def test_func(self, **kwargs):
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        text_error = translate("You are not allowed to edit this user")
        messages.error(self.request, text_error)
        return redirect(reverse_lazy('users'))


class UserDeleteView(
    UserPassesTestMixin,
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView
):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'forms.html'
    success_message = translate("User successfully deleted")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = translate('Delete user')
        context['value_to_delete'] = context['object']
        context['name'] = translate('user')
        context['button'] = translate('Delete')
        return context

    def test_func(self, **kwargs):
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        text_error = translate("You are not allowed to delete this user")
        messages.error(self.request, text_error)
        return redirect(reverse_lazy('users'))


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'forms.html'
    success_message = translate("You are logged in")  # "Вы залогинены"
    error_message = translate(
        "Please check if your login or password is correct"
    )
    extra_context = {
        'title': translate('Log In'),
        'button': translate('Log In'),
    }

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        msg = translate("Successfully logged out")
        messages.add_message(request, messages.INFO, msg)
        return response
