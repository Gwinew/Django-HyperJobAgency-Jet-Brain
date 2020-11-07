from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden

class MainPage(View):
    def get(self, request):
        return render(request, "hyperjob/mainpage.html")

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = "hyperjob/login.html"

class MySignUp(CreateView):
    form_class = UserCreationForm
    success_url = "login"
    template_name = "hyperjob/signup.html"

class ProfilePage(View):
    def get(self, request):
        return render(request, 'hyperjob/home_page.html')

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if request.user.is_staff == True:
                description = request.POST.get('description')
                Vacancy.objects.create(author=request.user, description=description)
                return redirect('/home')
            else:
                description = request.POST.get("description")
                Resume.objects.create(author=request.user, description=description)
                return redirect('/home')