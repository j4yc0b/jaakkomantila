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
    context = {'projects':projects}
    return render(request,'projects/aboutme.html', context)

def user_profile(request, pk):
    projects = Project.objects.all()

    # top_skills = projects.skill_set.exclude(title__exact="")
    skills = projects.skill_set.filter(title="Example3")

    context = {'projects': projects, 'skills': skills}

    return render(request,'projects/aboutme.html',context)
