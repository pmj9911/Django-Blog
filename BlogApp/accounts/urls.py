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
from django.urls import path , re_path
from . import views

app_name = "accounts"
# re_path is a variable which works with regular expressions
urlpatterns = [
    path('signup/',views.signup_view, name="signup"),
    path('login/',views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    re_path('profile/(?P<Username>[\w-]+)/', views.profile_view, name="profile"),

]


 #just some random shit for testing git