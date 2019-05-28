from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from django.contrib.auth.decorators import login_required
from .models import Profile
def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             login(request, user)
             return redirect('accounts:register')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

@login_required(login_url="/accounts/login/")
def register_view(request):
    if request.method == "POST":
        form = forms.CreateProfile(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Username = request.user
            instance.linker= instance.First_Name + "-" + instance.Last_Name
            instance.save()
            return redirect('ArticlesApp:list')
    else:
        form = forms.CreateProfile()
    return render(request, 'accounts/register.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else: 
                return redirect('ArticlesApp:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('ArticlesApp:list')

def profile_view(request,Username):
    profile = Profile.objects.get(Username=Username)
    return render(request, 'accounts/profile.html',{'profile': profile})