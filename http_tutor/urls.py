from django.urls import path

from . import views

app_name = 'http_tutor'
urlpatterns = [
    path('', views.index, name='index')
]