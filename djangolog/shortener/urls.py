
from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.shorten_url, name='short'),
]