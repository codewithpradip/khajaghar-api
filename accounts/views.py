from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

# 
class UserRegister(APIView):

    """
    Handles user Registration.
    """
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({
                'msg':'user registration success !!!',
                'token':token,},
                status=status.HTTP_201_CREATED)

class UserLogin(APIView):
    """
    Handles user login.
    """
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
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
                    'error':{'non_field_error':['Email and Password is not valid']}},
                    status=status.HTTP_401_UNAUTHORIZED)

class UserProfile(APIView):
    """
    Handel User Profile
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK)
