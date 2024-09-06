from django.urls import path
from statuses imprt views


urlpatterns = [
    path('', views.StatusesAllView.as_view(), name='statuses'),
]