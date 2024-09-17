from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from statuses.models import Status
from statuses.forms import StatusCreateForm
from utils.utils_classes import CustomLoginRequiredMixin
from django.utils.translation import gettext as translate
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
# Create your views here.

class StatusesAllView(CustomLoginRequiredMixin, View):
    def get(self, request):
        tables = [
            'ID',
            'Name',
            'Created at',
            'Action',
        ]
        
        all_statuses = Status.objects.all()
        info = []
        for item in all_statuses:
            info.append(
                (
                    item.id,
                    item.title,
                    item.created_at,
                )
            )
        return render(request, 'table.html', context={
            'info': info,
            'tables': tables,
            'title': translate('Statuses'),
            'url_name_change': 'update_status',
            'url_name_delete': 'delete_status',
        })

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
    template_name = 'forms.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value_to_delete'] = context['object']
        context['name'] = translate('status')
        context['button'] = translate('delete')
        return context
    