from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from statuses.models import Status
from statuses.forms import StatuseCreateForm
from utils.utils_classes import CustomLoginRequiredMixin
from django.utils.translation import gettext as translate
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
# Create your views here.

class StatusesAllView(CustomLoginRequiredMixin, View):
    def get(self, request):
        all_statuses = Status.objects.all()
        return render(request, 'statuses/statuses.html', context={
            'all_statuses': all_statuses,
        })

class StatusCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatuseCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('home')
    success_message = translate("Status created successfully")
    extra_context = {
        'title': translate('Create status'),
        'value': translate('Create'),
    }


class StatusUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['title']
    template_name = 'forms.html'
    success_url = reverse_lazy('home')
    success_message = translate("Status updated successfully")
    extra_context = {
        'title': translate('Update status'),
        'value': translate('Update'),
    }


class StatusDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('home')
    success_message = translate('Status deleted successfully')
    template_name = 'forms.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_to_delete'] = context['object']
        context['value'] = translate('delete')
        return context
    