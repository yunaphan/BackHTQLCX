from accounts.Serializers.TenCXSerializer import TenCXSeria
from accounts.Models.TenCXModel import Tencx
from rest_framework import viewsets, generics
from accounts.permissions import IsAdmin
from rest_framework import permissions

class TenCXView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = TenCXSeria
    queryset = Tencx.objects.using('DoThi').all()
