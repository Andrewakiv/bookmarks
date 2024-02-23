from django.contrib.auth.views import (PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path, reverse_lazy

from project import settings
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('login/', views.login_view, name='login'),
    # if we want to use Login/outView or PasswordChangeView here, we also must create registration/ dir
    # in templates and register our app before contrib.auth
    path('login/', views.LoginUser.as_view(), name='login'),
    # also can provide logout with template_name= and don't create a class
    path('logout/', views.LogoutUser.as_view(), name='logout'),

    path('password-change/', views.UserChangePassword.as_view(), name='password_change'),
    path('password-change_done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),

    path('password-reset/', PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        email_template_name='accounts/password_reset_email.html',
        success_url=reverse_lazy('accounts:password_reset_done')
    ), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_form.html',
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
