from rest_framework import viewsets
from accounts.Models.TrangThaiCXModel import Trangthaicx
from accounts.Serializers.TrangThaiCXSerializer import TrangThaiCXSeria
from accounts.permissions import IsAdmin
from rest_framework import permissions

class TrangThaiCayXanhView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = TrangThaiCXSeria
    queryset = Trangthaicx.objects.using('DoThi').all()
