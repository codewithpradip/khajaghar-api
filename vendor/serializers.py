from rest_framework import serializers
from .models import User, Vendor

class VendorRegistrationSerializer(serializers.ModelSerializer):
    # Include extra fields for Vendor profile
    vendor_name = serializers.CharField(max_length=100)
    vendor_license = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = ['name','username', 'email', 'password', 'vendor_license', 'vendor_name']
        extra_kwargs = {
            'password': {'write_only': True},  # Do not return passwords in responses
        }

    def create(self, validated_data):
        # Extract Vendor-specific fields
        vendor_data = {
            'vendor_name': validated_data.get('vendor_name'),
        }

        # Create User with role='vendor'
        user = User.objects.create_user(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
         
        )
        user.role = User.VENDOR
        user.save()

        # Create associated Vendor profile
        Vendor.objects.create(user=user, **vendor_data)
        return user

class VendorLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']