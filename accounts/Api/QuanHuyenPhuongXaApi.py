from rest_framework import viewsets, generics
from accounts.Models.QuanHuyenPhuongXaModel import Quanhuyen, Phuongxa
from accounts.Serializers.QuanHuyenPhuongXaSeria import QuanHuyenSeria, PhuongXaSeria
from accounts.permissions import IsAdmin
from rest_framework import permissions

class QuanHuyenView(viewsets.GenericViewSet, generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = QuanHuyenSeria
    queryset = Quanhuyen.objects.values('objectid', 'maquanhuyen',
                                                       'tenquanhuyen', 'matinh',
                                                       'loai', 'tenkhongdau')

class PhuongxaView(viewsets.GenericViewSet, generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = PhuongXaSeria
    queryset = Phuongxa.objects.using('DoThi').values('objectid', 'maquanhuyen',
                                                      'maphuongxa', 'tenphuongxa',
                                                      'loai', 'tenkhongdau')
