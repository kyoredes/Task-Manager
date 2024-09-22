from django.urls import path
from labels import views

urlpatterns = [
    path('', views.labels, name='labels'),
    path('create/', views.LabelCreateView.as_view(), name='create_label'),
    path('update/', views.LabelUpdateView.as_view(), name='update_label'),
    path('delete/', views.LabelDeleteView.as_view(), name='delete_label'),
]