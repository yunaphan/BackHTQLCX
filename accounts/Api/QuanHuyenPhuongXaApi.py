from rest_framework import viewsets, generics
from accounts.Models.QuanHuyenPhuongXaModel import Quanhuyen, Phuongxa
from accounts.Serializers.QuanHuyenPhuongXaSeria import QuanHuyenSeria, PhuongXaSeria

class QuanHuyenView(viewsets.GenericViewSet, generics.ListAPIView):
    serializer_class = QuanHuyenSeria
    queryset = Quanhuyen.objects.using('DoThi').values('objectid', 'maquanhuyen',
                                                       'tenquanhuyen', 'matinh',
                                                       'loai', 'tenkhongdau')

class PhuongxaView(viewsets.GenericViewSet, generics.ListAPIView):
    serializer_class = PhuongXaSeria
    queryset = Phuongxa.objects.using('DoThi').values('objectid', 'maquanhuyen',
                                                      'maphuongxa', 'tenphuongxa',
                                                      'loai', 'tenkhongdau')
