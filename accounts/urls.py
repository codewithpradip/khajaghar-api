from django.urls import path
from accounts.views import UserRegister, UserLogin, UserProfile
urlpatterns = [
   path("register/", UserRegister.as_view(), name='userregister'),
   path("login/", UserLogin.as_view(), name='userlogin'),
   path("userprofile/", UserProfile.as_view(), name='userprofile'), 
]