from django.contrib import admin
from accounts import urls
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include('accounts.urls')),
]
