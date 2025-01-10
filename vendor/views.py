from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VendorRegistrationSerializer, VendorLoginSerializer
from django.contrib.auth import authenticate
from accounts.views import get_tokens_for_user

class VendorRegister(APIView):
    """
    Handles vendor Registration.
    """
    def post(self, request):
        serializer = VendorRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"message": "Vendor registered successfully!"},
                status=status.HTTP_201_CREATED
            )


class VendorLogin(APIView):
    """
    Handles user login.
    """
    def post(self, request, format=None):
        serializer = VendorLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({
                    'msg':'login successfull',
                    'token':token},
                    status=status.HTTP_200_OK)
            else:
                return Response({
                    'error':{'non_field_error':['Email and Password is not valid!']}},
                    status=status.HTTP_401_UNAUTHORIZED)

