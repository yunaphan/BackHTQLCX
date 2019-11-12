from rest_framework import viewsets, generics
from accounts.Models.TimDuongModel import Timduong
from accounts.Serializers.DuongSerializer import DuongSeria
from accounts.permissions import IsAdmin
from rest_framework import permissions

class DuongView(viewsets.GenericViewSet, generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = DuongSeria
    queryset = Timduong.objects.using('DoThi').values('objectid', 'maduong', 'tenduong')