from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.UserShowView.as_view(), name='users'),
    path('create/', views.UserCreateView.as_view(), name='registrate'),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.UserDeleteView.as_view(), name='delete'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]