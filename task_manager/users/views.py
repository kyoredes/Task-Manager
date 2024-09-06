from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as translate


class UserShowView(View):
    def get(self, request):
        all_users = User.objects.all()
        return render(request, 'users/users.html', context={
            'all_users': all_users})


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = CreateUserForm
    template_name = 'users/reg.html'
    success_url = reverse_lazy('home')
    success_message = translate("User registered successfully")  #"Пользователь успешно зарегистрирован"



class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'password']
    template_name = 'users/upd.html'
    success_url = reverse_lazy('home')
    success_message = translate("User successfully changed")  # "Пользователь успешно изменен"


class UserDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'users/del.html'
    success_message = translate("User successfully deleted")  # "Пользователь успешно удален"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_to_delete'] = context['object']
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/log.html'
    success_message = translate("You are logged in")  # "Вы залогинены"
    
    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        msg = translate("Successfully logged out")
        messages.add_message(request, messages.INFO, msg)
        return response
