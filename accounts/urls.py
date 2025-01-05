from django.urls import path
from accounts.views import UserRegister, UserLogin, UserProfile
urlpatterns = [
   path("register/", UserRegister.as_view(), name='register'),
   path("login/", UserLogin.as_view(), name='login'),
   path("userprofile/", UserProfile.as_view(), name='profile')
]