from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    global user
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'username already taken'})
            except User.DoesNotExist:
                User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'passwords must match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    # TODO need to route
    return render(request, 'accounts/signup.html')
