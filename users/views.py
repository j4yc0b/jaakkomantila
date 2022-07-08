from django.shortcuts import render
from .models import Profile
from .models import Skill

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)
    
def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

def aboutme(request):
    project_obj = Profile.objects.get(name='Jaakko Mantila')
    context = {'info':project_obj}
    return render(request,'users/aboutme.html', context)

def skills(request):
    skillObj = Skill.objects.all()
    context = {'skills':skillObj}
    return render(request,'users/aboutme.html',context)

