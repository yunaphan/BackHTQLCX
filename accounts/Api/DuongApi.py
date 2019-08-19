from rest_framework import viewsets, generics
from accounts.Models.TimDuongModel import Timduong
from accounts.Serializers.DuongSerializer import DuongSeria

class DuongView(viewsets.GenericViewSet, generics.ListAPIView):
    serializer_class = DuongSeria
    queryset = Timduong.objects.using('DoThi').values('objectid', 'maduong', 'tenduong')