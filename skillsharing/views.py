from django.shortcuts import render
from .models import Skill
# Create your views here.

def skills(request):
    skills = Skill.objects.all()
    context = {'skills':skills}
    return render(request,'skills.html',context)