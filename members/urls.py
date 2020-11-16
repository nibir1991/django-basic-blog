"""MyBLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from .views import UserRegistration,UserUpdate,PasswordChange,PasswordSuccess,ShowProfile,EditProfile
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
   path('register/', UserRegistration.as_view(),name='register'),
   path('edit_profile/', UserUpdate.as_view(),name='edit_profile'), 
   path('password/', PasswordChange.as_view(template_name='registration/change_password.html')),
   path('password_success/',PasswordSuccess, name='password_success'),
   path('<int:pk>/profile/', ShowProfile.as_view(),name='show_profile'),
   path('<int:pk>/edit_profile_page/', EditProfile.as_view(),name='edit_profile_page'),
]
