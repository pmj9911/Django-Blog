"""BlogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views


app_name = "accounts"
# re_path is a variable which works with regular expressions
urlpatterns = [
    path('signup/',views.signup_view, name="signup"),
    path('login/',views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('profile/', views.profile_view, name="profile"),
    path('updateProfile/', views.profile_update, name="update"),
    # path('', include('django.contrib.auth.urls')),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
         {"post_rest_redirect":"accounts:password_change_done"},name='password-reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
