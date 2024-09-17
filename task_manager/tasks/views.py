from django.shortcuts import render
from .models import Task
from django.urls import reverse_lazy
from django.utils.translation import gettext as translate
from django.contrib.messages.views import SuccessMessageMixin
from utils.utils_classes import CustomLoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from tasks.forms import TaskCreateForm
from tasks.models import Task
# Create your views here.
def tasks(request):
    all_tasks = Task.objects.all()
    info = []
    for item in all_tasks:
        info.append(
            [
                item.id,
                item.title,
                item.status,
                item.author,
                item.executor,
                item.created_at
            ]
        )
    tables = [
        translate('ID'),
        translate('Name'),
        translate('Status'),
        translate('Author'),
        translate('Executor'),
        translate('Created at'),
        translate('Action'),
    ]
    return render(request, 'table.html', context={
        'info': info,
        'title': 'Tasks',
        'tables': tables,
        'url_name_change': 'update_task',
        'url_name_delete': 'delete_task',
        'button_value': translate('Create task'),
        'button_url': reverse_lazy('create_task')
    })


class TaskCreateView(SuccessMessageMixin, CustomLoginRequiredMixin, CreateView):
    form_class = TaskCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('home')
    success_message = translate('Task created successfully')
    extra_context = {
        'title': 'Create task',
        'button': translate('Create'),
    }
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, CustomLoginRequiredMixin, UpdateView):
    model = Task
    success_message = translate("Task successfully updated")
    success_url = reverse_lazy('home')
    template_name = 'forms.html'
    fields = ['title', 'description', 'status', 'executor']
    extra_context = {
        'title': translate('Update task'),
        'button': translate('Update'),
    }


class TaskDeleteView(SuccessMessageMixin, CustomLoginRequiredMixin, DeleteView):
    model = Task
    success_message = translate('Task deleted successfully')
    success_url = reverse_lazy('home')
    template_name = 'forms.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = translate('Delete task')
        context['value_to_delete'] = context['object']
        context['name'] = translate('task')
        context['button'] = translate('delete')
        return context

