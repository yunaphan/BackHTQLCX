from accounts.models import Chucnangnguoidung, Chucnang, Quyennguoidung
from accounts.Serializers.PhanQuyenSerializer import ChucNangSerializer, ChucnangnguoidungSerializer, QuyenNguoiDungSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class ChucNangView(viewsets.ModelViewSet):
    queryset = Chucnang.objects.all()
    serializer_class = ChucNangSerializer
    lookup_field = "machucnang"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['machucnang']

class QuyenNguoiDungView(viewsets.ModelViewSet):
    queryset = Quyennguoidung.objects.all()
    serializer_class = QuyenNguoiDungSerializer
    lookup_field = "maquyen"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['maquyen']

class ChucNangNguoiDungView(viewsets.ModelViewSet):
    queryset = Chucnangnguoidung.objects.all()
    serializer_class = ChucnangnguoidungSerializer
    lookup_field = "machucnangnguoidung"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['machucnang', 'maquyen']