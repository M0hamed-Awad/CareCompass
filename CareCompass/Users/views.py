from django.shortcuts import render, redirect
from .forms import  RegistrationForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.views import LoginView

# Create your views here.


# Login

class MyLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, 'You Have Logged In Successfully!')
        return super().form_valid(form)

# Registration

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account Has Been Created Successfully!')
            return redirect('login')
    else:
        form = RegistrationForm()
        
    context =  {"form": form}
    return render(request, 'Users/sign_up.html', context)


# Logout

def my_logout(request):
    auth.logout(request)
    return redirect('login')


# User Profile

@login_required(login_url= "login")
def update_user_profile(request):
    user = request.user

    if request.method == 'POST':
        user_info_form = UserForm(request.POST, instance=user)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)

        if user_info_form.is_valid() and user_profile_form.is_valid():
            user_info_form.save()
            user_profile_form.save()
            messages.success(request, 'Your Profile Has Been Updated successfully!')
            return redirect('user_profile')

    else:
        user_info_form = UserForm(instance=user)
        user_profile_form = UserProfileForm(instance=user.userprofile)


    context = {
        'user_form': user_info_form,
        'profile_form': user_profile_form,
    }
    
    return render(request, 'Users/user-profile.html', context)
    
