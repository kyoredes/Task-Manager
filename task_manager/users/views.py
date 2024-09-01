from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
# from users.models import User
# from users.forms import UsersCreateForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.views import LoginView
# from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from users.forms import CreateUserForm
from django.urls import reverse_lazy


class UserShowView(View):
    def get(self, request):
        all_users = User.objects.all()
        return render(request, 'users/users.html', context={
            'all_users': all_users})


class UserCreateView(CreateView):
    form_class = CreateUserForm
    template_name = 'users/reg.html'
    success_url = reverse_lazy('home')


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'password']
    template_name = 'users/upd.html'
    success_url = reverse_lazy('home')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'users/del.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_to_delete'] = context['object']
        return context


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/log.html'
    def get_success_url(self):
        return reverse_lazy('home')
        

# class UsersLoginView(View):
#     def get(self, request, *args, **kwargs):
#         form = UsersLoginForm()
#         return render(request, 'log.html', context={
#             'form': form,
#         })
#     def post(self, request, *args, **kwargs):
#         form = UsersLoginForm(request.POST)
#         if form:
#             return redirect('home')
#         return render(request, 'log.html', context={
#             'form': form
#         })

# class UsersUpdateView(View):
#     def get(self, request):
#         return render(request, 'upd.html')
#     def post(self, request):
#         return render(request, 'upd.html')


# class UsersDeleteView(View):
#     def get(self, request):
#         return render(request, 'del.html')
#     def post(self, request):
#         return render(request, 'del.html')
