from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Doctors.models import DoctorProfile
from django.db.models import Q
from Home.utils import get_current_locations_and_specialties
from Doctors.utils import specialty_icons

# Create your views here.

@login_required(login_url= "login")
def search_doctors(request):
    filtered_doctors = []
    
    areas, specialties = get_current_locations_and_specialties()
    
    if request.method == 'GET':
        searched_area = request.GET.get('Area')
        searched_specialty = request.GET.get('Specialty')
        # (no filter)
        filters = Q()

        if searched_area:
            filters = filters & Q(address_in_english__contains=searched_area)

        if searched_specialty:
            filters = filters & Q(specialization_in_english__exact=searched_specialty)

        # Apply filters to the query
        filtered_doctors = DoctorProfile.objects.filter(filters).distinct()
    
    context = {
        "doctors": filtered_doctors,
        "areas": areas,
        "specialties": specialties,
    }
    return render(request, 'Search/searched_doctors.html', context)



@login_required(login_url= "login")
def specialized_doctors(request):
    
    if request.method == 'GET':
        specialty = request.GET.get('specialty')
        doctors = DoctorProfile.objects.filter(specialization_in_english__exact=specialty)
        specialty_icon = specialty_icons[specialty]
    
    context = {
        'doctors': doctors,
        'specialty': specialty,
        'specialty_icon': specialty_icon,
    }
    
    return render(request, 'Search/specialized_doctors.html', context)