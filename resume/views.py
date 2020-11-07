from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from django.http import HttpResponseForbidden


# Create your views here.

class ResumeList(View):
    def get(self, request):
        return render(request, "resume/resume_list.html", {'resume': Resume.objects.all()})

class ResumeNew(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            return render(request,"resume/resume_new.html")

    def post(self, request):
        description = request.POST.get("description")
        Resume.objects.create(author=request.user, description=description)
        return redirect('/home')


#        description = request.POST.get("description")
#        Resume.objects.filter(author=request.user).update(description=description)
#        return redirect('/home')

