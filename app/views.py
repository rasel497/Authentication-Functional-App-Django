from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
                
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, 'Login successfully')
            return redirect('dashboard')

        else:
            messages.warning(request, 'Invalid username or password')
    return render(request, 'app/login.html')


def register_view(request):
    return render(request, 'app/regiter.html')

def dashboard_view(request):
    return render(request, 'app/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
