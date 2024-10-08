from task_manager.labels.models import Label
from django.utils.translation import gettext as translate
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from task_manager.labels.forms import LabelCreateForm
from task_manager.utils.utils_classes import CustomLoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.deletion import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect


class LabelListView(ListView):
    model = Label
    template_name = 'table.html'
    context_object_name = 'info'
    paginate_by = 20
    tables = [
        'ID',
        translate('Name'),
        translate('Created at'),
        translate('Action'),
    ]
    extra_context = {
        'title': translate('Label'),
        'tables': tables,
        'url_name_change': 'update_label',
        'url_name_delete': 'delete_label',
        'button_value': translate('Create label'),
        'button_url': reverse_lazy('create_label'),
    }

    def get_queryset(self):
        return Label.objects.values(
            'id',
            'name',
            'created_at',
        )


class LabelCreateView(
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    form_class = LabelCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('labels')
    success_message = translate("Label created successfully")
    extra_context = {
        'title': translate('Create label'),
        'button': translate('Create'),
    }


class LabelUpdateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    UpdateView,
):
    form_class = LabelCreateForm
    template_name = 'forms.html'
    success_message = translate('Label successfully changed')
    success_url = reverse_lazy('labels')
    extra_context = {
        'title': translate('Update label'),
        'button': translate('Update'),
    }

    def get_queryset(self):
        return Label.objects.all()


class LabelDeleteView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    DeleteView,
):
    model = Label
    success_message = translate('Label deleted successfully')
    success_url = reverse_lazy('labels')
    template_name = 'forms.html'
    error_message = translate('This label is in use')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = translate('Delete Label')
        context['value_to_delete'] = context['object']
        context['name'] = translate('label')
        context['button'] = translate('Yes, delete')
        return context

    def post(self, request, *args, **kwargs):
        label = self.get_object()

        try:
            label.delete()
            messages.success(request, self.success_message)
        except ProtectedError:
            messages.error(request, self.error_message)
        return redirect(self.success_url)

    def handle_no_permission(self):
        text_error = translate('This label is in use')
        messages.error(self.request, text_error)
        return redirect(reverse_lazy('labels'))
