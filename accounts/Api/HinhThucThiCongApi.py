from rest_framework import viewsets
from accounts.Models.HinhThucThiCongModel import Hinhthucthicong
from accounts.Serializers.HinhThucThiCongSerializer import HinhThucThiCongSeria
from accounts.permissions import IsAdmin
from rest_framework import permissions

class HinhThucThiCongView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = HinhThucThiCongSeria
    queryset = Hinhthucthicong.objects.all()
    lookup_field = "maloai"