from django.shortcuts import render
from users.models import Profile

def navbar(request):
    project_obj = Profile.objects.get(name='Jaakko Mantila')
    context = {'navbar':project_obj}
    return render(request, 'navbar.html', context)