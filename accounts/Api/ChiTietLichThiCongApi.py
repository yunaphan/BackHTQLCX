from accounts.models import ChiTietThiCong
from accounts.Serializers.ChiTietLichThiCongSerializer import ChiTietLichThiCongSerializer
from rest_framework import viewsets
from accounts.permissions import IsAdmin
from rest_framework import permissions

class ChiTietLichThiCongView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = ChiTietThiCong.objects.all()
    serializer_class = ChiTietLichThiCongSerializer