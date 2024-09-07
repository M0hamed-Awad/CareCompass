from django.shortcuts import render, get_object_or_404
from .models import DoctorProfile
from .utils import specialty_icons

# Create your views here.

def doctor_profile(request):
    doctor_id = request.GET['id']
    
    doctor = get_object_or_404(DoctorProfile, id=doctor_id)
    
    doctor_specialty_icon = specialty_icons[doctor.specialization_in_english]
    
    context = {"doctor": doctor , "doctor_specialty_icon": doctor_specialty_icon}
    
    return render(request, 'Doctors/doctor_profile.html', context)