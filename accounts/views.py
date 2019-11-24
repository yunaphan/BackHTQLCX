from rest_framework.views import APIView
from django.contrib.auth import login, logout, get_user_model
from rest_framework import viewsets, response, status, permissions
from rest_framework.permissions import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.authtoken.models import Token
from accounts.permissions import IsAdmin
from . import serializers
from .serializers import UserCreationSerializer, LoginSerializer
from rest_framework.parsers import FileUploadParser, FormParser, JSONParser, MultiPartParser
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from accounts.models import NhomThiCong
from accounts.serializers import NhomTCSerializer
User = get_user_model()

class NhomThiCongView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = NhomTCSerializer
    queryset = NhomThiCong.objects.all()
    lookup_field = "manhomthicong"

class ListUserView(viewsets.GenericViewSet, ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()

class RegisterView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    parser_class = (FileUploadParser, MultiPartParser, FormParser, JSONParser)
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetriveUserView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()
    lookup_field = "username"

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

