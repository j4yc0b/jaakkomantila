from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
# from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    project_obj = Project.objects.get(id=pk)
                                                        #the name used in the template == 'project'
    return render(request,'projects/single-project.html',{'project':project_obj})

# def aboutme(request):
#     project_obj = Project.objects.get(title='Example3')
#     context = {'info':project_obj}
#     return render(request,'projects/aboutme.html', context)

# def user_profile(request, pk):
#     projects = Project.objects.all()

#     skills = projects.skill_set.filter(title="Example3")

#     context = {'projects': projects, 'skills': skills}

#     return render(request,'projects/aboutme.html',context)
