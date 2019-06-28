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
            request.user.Email_Address = instance.Email_Address
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

@login_required(login_url="/accounts/login/")
def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('ArticlesApp:list')

@login_required(login_url="/accounts/login/")
def profile_view(request):
#    # profile = Profile.objects.get(Username=Username)
    return render(request, 'accounts/profile.html')

@login_required(login_url="/accounts/login/")
def profile_update(request):
    if request.method == 'POST':
        form = forms.UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = forms.UpdateProfile(instance=request.user.profile)
    return render(request,'accounts/updateProfile.html', { 'form':form })