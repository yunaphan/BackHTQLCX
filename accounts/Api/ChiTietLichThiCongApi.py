from accounts.models import ChiTietThiCong
from accounts.Serializers.ChiTietLichThiCongSerializer import ChiTietLichThiCongSerializer
from rest_framework import viewsets
from accounts.permissions import IsAdmin
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F

class ChiTietLichThiCongView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = ChiTietThiCong.objects.all().order_by(F('NgayBD').desc())
    serializer_class = ChiTietLichThiCongSerializer
    lookup_field = "macttc"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tuyenduong', 'lichthicong', 'NgayBD', 'nhomthiconglich', 'trangthaitc']
