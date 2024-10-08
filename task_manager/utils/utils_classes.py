from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as translate
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            text_error = translate("You are not logged in! Please sign in.")
            messages.error(request, text_error)
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)
