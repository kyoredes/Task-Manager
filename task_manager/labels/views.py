from django.shortcuts import render
from labels.models import Label
from django.utils.translation import gettext as translate
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from labels.forms import LabelCreateForm

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
            'button_url': reverse_lazy('create_lable')
        }
    )

class LabelCreateView(CreateView):
    form_class = LabelCreateForm
    

class LabelUpdateView(UpdateView):
    pass

class LabelDeleteView(DeleteView):
    pass