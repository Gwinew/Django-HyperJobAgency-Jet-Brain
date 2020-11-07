"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import MainPage, MyLoginView, MySignUp, ProfilePage
from resume.views import ResumeList, ResumeNew
from vacancy.views import VacanciesList, VacancyNew
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('resumes', ResumeList.as_view()),
    path('vacancies', VacanciesList.as_view()),
    path('login', MyLoginView.as_view()),
    path('signup', MySignUp.as_view()),
    path('logout', LogoutView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('resume/new', ResumeNew.as_view()),
    path('vacancy/new', VacancyNew.as_view()),
    path('home', ProfilePage.as_view())
]
