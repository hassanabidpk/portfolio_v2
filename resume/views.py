from django.shortcuts import render
from .models import Skill,Project

def index(request):
        projects = Project.objects.order_by('createdAt')
        context = {"projects":projects}
        return render(request,'resume/index.html', context)

def about(request):
    context = ''
    return render(request,'resume/about.html',context)

def contact(request):
    context = ''
    return render(request,'resume/contact.html',context)
