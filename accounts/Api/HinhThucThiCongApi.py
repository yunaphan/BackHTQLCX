from rest_framework import viewsets
from accounts.Models.HinhThucThiCongModel import Hinhthucthicong
from accounts.Serializers.HinhThucThiCongSerializer import HinhThucThiCongSeria

class HinhThucThiCongView(viewsets.ModelViewSet):
    serializer_class = HinhThucThiCongSeria
    queryset = Hinhthucthicong.objects.using('DoThi').all()