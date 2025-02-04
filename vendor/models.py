from django.db import models
from accounts.models import User

# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(
        User, related_name='user', 
        on_delete=models.CASCADE
        )
    vendor_name = models.CharField(max_length=50)
    vendor_license = models.ImageField(upload_to='vendor/license')
    description = models.TextField(blank=True, null=True, max_length=150)
    vendor_logo = models.ImageField(upload_to='vendor/logo' )
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name
