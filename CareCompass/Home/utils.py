from Doctors.models import DoctorProfile

def get_current_locations_and_specialties():
    
    current_locations = DoctorProfile.objects.values('address_in_english', 'address_in_arabic').distinct()
    current_specialties = DoctorProfile.objects.values('specialization_in_english', 'specialization_in_arabic').distinct().order_by('specialization_in_english')

    areas = set()
    
    for location in current_locations:
        english_area = location['address_in_english'].split(',')[-2].strip()
        arabic_area = location['address_in_arabic'].split('،')[-2].strip()
        areas.add((english_area, arabic_area))

    areas = list(areas)
    areas.sort()
 
    specialties = [(spec['specialization_in_english'], spec['specialization_in_arabic']) for spec in current_specialties]
    return areas,specialties