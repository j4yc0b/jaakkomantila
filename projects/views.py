from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj=Project.objects.get(id=pk)
    return render(request,'projects/single-project.html',{'project':projectObj})

def aboutme(request):
    projects = Project.objects.all()
    context = {'aboutme':aboutme}
    return render(request,'projects/aboutme.html', context)

