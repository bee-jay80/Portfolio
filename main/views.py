from django.shortcuts import render , get_object_or_404
from . models import Project,Tag,Skill

# Create your views here.

def home(request):
    projects = Project.objects.all()
    tag = Tag.objects.all()
    return render(request,"home.html",{"projects":projects,"tags":tag})

def contact(request):
    return render(request,"contact.html")

def project(request,id):
    project = get_object_or_404(Project,pk=id)
    return render(request,"project.html",{"project":project})

def about(request):
    skill = Skill.objects.all()
    return render(request,"about.html",{"skill":skill})