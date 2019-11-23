from accounts.models import Chucnangnguoidung, Chucnang, Quyennguoidung
from accounts.Serializers.PhanQuyenSerializer import ChucNangSerializer, ChucnangnguoidungSerializer, QuyenNguoiDungSerializer
from rest_framework import viewsets

class ChucNangView(viewsets.ModelViewSet):
    queryset = Chucnang.objects.all()
    serializer_class = ChucNangSerializer
    lookup_field = "chucnang"

class QuyenNguoiDungView(viewsets.ModelViewSet):
    queryset = Quyennguoidung.objects.all()
    serializer_class = QuyenNguoiDungSerializer
    lookup_field = "quyennguoidung"

class ChucNangNguoiDungView(viewsets.ModelViewSet):
    queryset = Chucnangnguoidung.objects.all()
    serializer_class = ChucnangnguoidungSerializer
    lookup_field = "machucnangnguoidung"