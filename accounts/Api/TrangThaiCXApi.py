from rest_framework import viewsets
from accounts.Models.TrangThaiCXModel import Trangthaicx
from accounts.Serializers.TrangThaiCXSerializer import TrangThaiCXSeria

class TrangThaiCayXanhView(viewsets.ModelViewSet):
    serializer_class = TrangThaiCXSeria
    queryset = Trangthaicx.objects.using('DoThi').all()
