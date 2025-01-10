from django.urls import path
from vendor.views import VendorRegister, VendorLogin

urlpatterns = [
    path('register/', VendorRegister.as_view(), name='vendorregister'),
    path('login/', VendorLogin.as_view(), name='vendorlogin')
]