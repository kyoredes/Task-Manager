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
        'ID',
        translate('Name'),
        translate('Status'),
        translate('Author'),
        translate('Executor'),
        translate('Created at'),
        translate('Action'),
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = translate('Tasks')
        context['tables'] = self.tables
        context['url_name_change'] = 'update_task'
        context['url_name_delete'] = 'delete_task'
        context['button_value'] = translate('Create task')
        context['button_url'] = reverse_lazy('create_task')
        context['task_filter'] = self.filterset
        context['list_name'] = 'Tasks'
        return context

    def get_queryset(self):
        queryset = Task.objects.select_related('author', 'status').values(
            'id',
            'name',
            'status__name',
            'author__first_name',
            'author__last_name',
            'executor__first_name',
            'executor__last_name',
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
    success_url = reverse_lazy('tasks')
    success_message = translate('Task created successfully')
    extra_context = {
        'title': translate('Create task'),
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
    form_class = TaskCreateForm
    success_message = translate("Task successfully updated")
    success_url = reverse_lazy('tasks')
    template_name = 'forms.html'
    extra_context = {
        'title': translate('Update task'),
        'button': translate('Update'),
    }

    def get_queryset(self):
        return Task.objects.all()


class TaskDeleteView(
    UserPassesTestMixin,
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    DeleteView
):
    model = Task
    success_message = translate('Task deleted successfully')
    success_url = reverse_lazy('tasks')
    error_url = translate("Task can only be deleted by its author")
    template_name = 'forms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = translate('Delete task')
        context['value_to_delete'] = context['object']
        context['name'] = translate('task')
        context['button'] = translate('Yes, delete')
        return context

    def test_func(self, **kwargs):
        return self.request.user.id == self.model.objects.all().get(
            id=self.kwargs.get('pk')
        ).author_id

    def handle_no_permission(self):
        text_error = translate("You are not allowed to delete this task")
        messages.error(self.request, text_error)
        return redirect(reverse_lazy('tasks'))


class TaskDetailView(DeleteView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'info'
