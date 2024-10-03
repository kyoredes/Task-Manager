from django.shortcuts import redirect
from task_manager.tasks.models import Task
from django.urls import reverse_lazy
from django.utils.translation import gettext as translate
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.utils.utils_classes import CustomLoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from task_manager.tasks.forms import TaskCreateForm
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from task_manager.tasks.filters import TaskFilter


class TaskListView(ListView):
    model = Task
    template_name = 'table.html'
    context_object_name = 'info'
    paginate_by = 20
    tables = [
        translate('ID'),
        translate('Name'),
        translate('Status'),
        translate('Author'),
        translate('Executor'),
        translate('Created at'),
        translate('Action'),
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task'
        context['tables'] = self.tables
        context['url_name_change'] = 'update_task'
        context['url_name_delete'] = 'delete_task'
        context['button_value'] = translate('Create task')
        context['button_url'] = reverse_lazy('create_task')
        context['task_filter'] = self.filterset
        return context

    def get_queryset(self):
        queryset = Task.objects.select_related('author', 'status').values(
            'id',
            'title',
            'status__title',
            'author__username',
            'executor__username',
            'created_at',
        )
        self.filterset = TaskFilter(
            self.request.GET,
            queryset=queryset,
            request=self.request
        )
        return self.filterset.qs


class TaskCreateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    CreateView
):
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


class TaskUpdateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    UpdateView
):
    model = Task
    success_message = translate("Task successfully updated")
    success_url = reverse_lazy('home')
    template_name = 'forms.html'
    fields = ['title', 'description', 'status', 'executor']
    extra_context = {
        'title': translate('Update task'),
        'button': translate('Update'),
    }


class TaskDeleteView(
    UserPassesTestMixin,
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    DeleteView
):
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

    def test_func(self, **kwargs):
        return self.request.user.id == self.model.objects.all().get(
            id=self.kwargs.get('pk')
        ).author_id

    def handle_no_permission(self):
        text_error = translate("You are not allowed to delete this task")
        messages.error(self.request, text_error)
        return redirect(reverse_lazy('tasks'))
