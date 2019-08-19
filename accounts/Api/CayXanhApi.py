from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from accounts.Serializers.CayXanhSerializer import CayXanhSerializer
from accounts.Models.CayXanhModel import Cayxanh

class CayXanhView(viewsets.GenericViewSet, ListAPIView):
    serializer_class = CayXanhSerializer
    queryset = Cayxanh.objects.using('DoThi').values('objectid', 'sohieu')