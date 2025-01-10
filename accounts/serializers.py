from rest_framework import serializers
from accounts.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'phone_number', 'password']

    # create user with role='customer'
    def create(self, validated_data):
        user = User.objects.create_user(
                name=validated_data['name'],
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
            )

        user.role = User.CUSTOMER
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email']
