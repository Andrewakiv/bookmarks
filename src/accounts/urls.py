from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from project import settings
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('login/', views.login_view, name='login'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
]
