from django.urls import path
from . import views
urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
]