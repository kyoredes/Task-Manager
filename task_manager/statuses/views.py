from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from statuses.models import Status
from statuses.forms import StatusCreateForm
from utils.utils_classes import CustomLoginRequiredMixin
from django.utils.translation import gettext as translate
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


class StatusesListView(ListView):
    model = Status
    template_name = 'table.html'
    context_object_name = 'info'
    paginate_by = 20
    tables = [
        translate('ID'),
        translate('Name'),
        translate('Created at'),
        translate('Action'),
    ]
    extra_context = {
        'title': 'Status',
        'tables': tables,
        'url_name_change': 'update_status',
        'url_name_delete': 'delete_status',
        'button_value': translate('Create status'),
        'button_url': reverse_lazy('create_status'),
    }

    def get_queryset(self):
        return Status.objects.values(
            'id',
            'title',
            'created_at',
        )


class StatusCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('home')
    success_message = translate("Status created successfully")
    extra_context = {
        'title': translate('Create status'),
        'button': translate('Create'),
    }


class StatusUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['title']
    template_name = 'forms.html'
    success_url = reverse_lazy('home')
    success_message = translate("Status updated successfully")
    extra_context = {
        'title': translate('Update status'),
        'button': translate('Update'),
    }


class StatusDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('home')
    success_message = translate('Status deleted successfully')
    error_message = translate("This status is in use")
    template_name = 'forms.html'
    
    def post(self, request, *args, **kwargs):
        status = self.get_object()

        try:
            status.delete()
            messages.success(request, self.success_message)
        except ProtectedError:
            messages.error(request, self.error_message)
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value_to_delete'] = context['object']
        context['name'] = translate('status')
        context['button'] = translate('delete')
        return context
    
