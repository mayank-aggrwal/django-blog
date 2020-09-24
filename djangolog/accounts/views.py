from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_page(request):
    if request.method == 'POST':
        print('login POST request received:', request.POST)
        form = AuthenticationForm(data=request.POST)
        print(form)
        print('login POST request received:', form.get_user())
        if form.is_valid():
            print('form is valid')
            user = form.get_user()
            login(request, user)
            print('redirecting')
            return redirect('articles:list')
        else:
            print('form is invalid')
    else:
        print('login GET request received')
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')