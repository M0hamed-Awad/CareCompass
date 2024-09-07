import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={ "placeholder" : "e.g., Mohamed" }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={ "placeholder" :"e.g., Awad" }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={ "placeholder" : "e.g., Mohamed.Awad@Gmail.Com"}))
    # Remove the password-based authentication field
    usable_password = None
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
    
        widgets = {
            'username': forms.TextInput(attrs={ "placeholder" : "e.g., Mohamed_Awad" }),
        }
        
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        
        help_texts = {
            'username': '150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        }
        
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_img", "phone_number", "city"]
        
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'e.g., 01012345678'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'e.g., Cairo'
            }),
        }
        
        help_texts = {
            'phone_number': 'Please enter a valid Egyptian phone number starting with [010 - 011 - 012 - 015].',
        }
        
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        # Regex (For Egypt Only)
        egypt_phone_regex = r'^(010|011|012|015)\d{8}$'
        
        if phone_number:
            if not re.match(egypt_phone_regex, phone_number):
                raise forms.ValidationError("Please enter a valid phone number.")
            
        return phone_number