from rest_framework.views import APIView
from .forms import UserCreationForm, UserLoginFroms
from django.contrib.auth import login, logout, get_user_model
from rest_framework import viewsets, response, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authtoken.models import Token
from . import serializers
from .serializers import UserCreationSerializer, LoginSerializer
User = get_user_model()

class RegisterView(viewsets.GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

class LoginView(APIView):
    def get_queryset(self):
        return User.objects.all()
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return response.Response({'key': token.key}, status=status.HTTP_202_ACCEPTED)

class LogoutView(APIView):
    def get_queryset(self):
        return User.objects.all()
    def post(self, request):
        logout(request)
        return response.Response(status=status.HTTP_200_OK)

class Tokenuser(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = serializers.TokenSerializer
    queryset = Token.objects.all()
