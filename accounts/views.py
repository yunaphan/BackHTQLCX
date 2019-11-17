from rest_framework.views import APIView
from django.contrib.auth import login, logout, get_user_model
from rest_framework import viewsets, response, status, permissions
from rest_framework.permissions import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.authtoken.models import Token
from accounts.permissions import IsAdmin
from . import serializers
from .serializers import UserCreationSerializer, LoginSerializer
User = get_user_model()

class RegisterView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

class LoginView(APIView):
    permission_classes = (AllowAny,)
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
    permission_classes = (AllowAny,)
    def get_queryset(self):
        return User.objects.all()
    def post(self, request):
        logout(request)
        return response.Response(status=status.HTTP_200_OK)

class Tokenuser(viewsets.GenericViewSet, ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = serializers.TokenSerializer
    queryset = Token.objects.all()

