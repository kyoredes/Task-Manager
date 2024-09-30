from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as translate
from django.contrib import messages


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        text_error = translate("You are not logged in! Please sign in.")
        messages.error(self.request, text_error)
        return super().handle_no_permission()
