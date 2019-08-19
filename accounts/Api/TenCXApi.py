from accounts.Serializers.TenCXSerializer import TenCXSeria
from accounts.Models.TenCXModel import Tencx
from rest_framework import viewsets, generics

class TenCXView(viewsets.ModelViewSet):
    serializer_class = TenCXSeria
    queryset = Tencx.objects.using('DoThi').all()
