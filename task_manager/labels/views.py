from django.shortcuts import render
from labels.models import Label
from django.utils.translation import gettext as translate
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from labels.forms import LabelCreateForm
from utils.utils_classes import CustomLoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def labels(request):
    all_labels = Label.objects.all()
    info = []
    for item in all_labels:
        info.append(
            [
                item.id,
                item.name,
                item.created_at,
            ]
        )
    tables = [
        translate('ID'),
        translate('Name'),
        translate('Created At'),
        translate('Action'),
    ]
    return render(
        request,
        'table.html',
        context={
            'info': info,
            'title': 'Labels',
            'tables': tables,
            'url_name_change': 'update_label',
            'url_name_delete': 'delete_label',
            'button_value': translate('Create label'),
            'button_url': reverse_lazy('create_label')
        }
    )

class LabelCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('home')
    success_message = translate("Label created successfully")
    extra_context = {
        'title': translate('Create label'),
        'button': translate('Create'),
    }


class LabelUpdateView(SuccessMessageMixin, CustomLoginRequiredMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'forms.html'
    success_message = translate('Label successfullt changed')
    success_url = reverse_lazy('labels')
    extra_context = {
        'title': translate('Update label'),
        'button': translate('Update'),
    }

class LabelDeleteView(SuccessMessageMixin, CustomLoginRequiredMixin, DeleteView):
    model = Label
    success_message = translate('Label deletes successfully')
    success_url = reverse_lazy('labels')
    template_name = 'forms.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = translate('Delete Label')
        context['value_to_delete'] = context['object']
        context['name'] = translate('label')
        context['button'] = translate('delete')
        return context

    def test_func(self, **kwargs):
        return True
    
    def handle_no_permission(self):
        text_error = translate('This label is in use')
        messages.error(self.request, text_error)
        return redirect(reverse_lazy('labels'))
