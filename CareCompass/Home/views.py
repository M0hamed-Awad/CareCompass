from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import get_current_locations_and_specialties

# Create your views here.

@login_required(login_url= "login")
def home(request):
    areas, specialties = get_current_locations_and_specialties()
    
    context = {
        "areas": areas,
        "specialties": specialties,
    }
    return render(request, 'Home/index.html', context)