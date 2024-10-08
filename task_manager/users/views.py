from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.users.forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext
from task_manager.utils.utils_classes import CustomLoginRequiredMixin
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
        'ID',
        gettext('Username'),
        gettext('Full name'),
        gettext('Created at'),
        gettext('Action'),
    ]
    extra_context = {
        'title': gettext('Users'),
        'tables': tables,
        'url_name_change': 'update_user',
        'url_name_delete': 'delete_user',
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
    success_url = reverse_lazy('login')
    success_message = gettext("User registered successfully")
    extra_context = {
        'title': gettext('Create User'),
        'button': gettext('Registrate'),
    }


class UserUpdateView(
    CustomLoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = User
    form_class = CreateUserForm
    template_name = 'forms.html'
    success_url = reverse_lazy('users')
    success_message = gettext("User successfully changed")
    extra_context = {
        'title': gettext('Update user'),
        'button': gettext('Update'),
    }

    def test_func(self, **kwargs):
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        text_error = gettext("You are not allowed to edit this user")
        messages.error(self.request, text_error)
        return redirect(reverse_lazy('users'))


class UserDeleteView(
    CustomLoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
):
    model = User
    success_url = reverse_lazy('users')
    template_name = 'forms.html'
    success_message = gettext("User successfully deleted")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Delete user')
        context['value_to_delete'] = context['object']
        context['name'] = gettext('user')
        context['button'] = gettext('Yes, delete')
        return context

    def test_func(self, **kwargs):
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        text_error = gettext("You are not allowed to delete this user")
        messages.error(self.request, text_error)
        return redirect(reverse_lazy('users'))


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'forms.html'
    success_message = gettext("You are logged in")  # "Вы залогинены"
    error_message = gettext(
        "Please check if your login or password is correct"
    )
    extra_context = {
        'title': gettext('Log In'),
        'button': gettext('Log in'),
    }

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        msg = gettext("Successfully logged out")
        messages.add_message(request, messages.INFO, msg)
        return response
