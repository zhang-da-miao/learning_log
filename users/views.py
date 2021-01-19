from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class Login(LoginView):
    LoginView.template_name = 'users/login.html'
    LOGIN_REDIRECT_URL = '/index'


class Logout(LogoutView):
    # LogoutView.template_name = 'users/logout.html'
    next_page = '/'

# def logout_view(request):
#     """注销用户"""
#     LogoutView(request)
#     return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
