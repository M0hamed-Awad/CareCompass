from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(template_name='Users/login.html'), name='login'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('logout', views.my_logout, name='logout'),
    path('user-profile', views.update_user_profile, name='user_profile'),
]