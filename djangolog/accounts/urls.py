
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_page),
    path('login/', views.login_page, name='login-page'),
]
