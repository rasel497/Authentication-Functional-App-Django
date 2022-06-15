#from atexit import register
#from email import message

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, 'Login successfully.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid username or password')
    return render(request, 'app/login.html')


def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration success, you can login now...')
            return redirect('login')

    return render(request, 'app/register.html', context={ 'form':form })

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'app/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')


#eikhne amra login url na diye project er setting thke global kore dile automatic login page chole jabe