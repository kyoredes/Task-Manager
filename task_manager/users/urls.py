from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('create/', views.UserCreateView.as_view(), name='create_user'),
    path(
        '<int:pk>/update/',
        views.UserUpdateView.as_view(),
        name='update_user'
    ),
    path(
        '<int:pk>/delete/',
        views.UserDeleteView.as_view(),
        name='delete_user'
    ),
]
