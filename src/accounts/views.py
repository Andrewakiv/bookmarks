from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import LoginForm, UserChangePasswordForm


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             username = cd['username']
#             password = cd['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#
#     return render(request, 'accounts/login.html', {'form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    extra_context = {'title': 'Authorization'}


class LogoutUser(LogoutView):
    # form_class = AuthenticationForm
    template_name = 'accounts/logout.html'
    extra_context = {'title': 'Logout'}


class UserChangePassword(PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')
