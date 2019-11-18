from rest_framework import viewsets, permissions
from accounts.models import LichThiCong
from accounts.Serializers.LichThiCongSerializer import LichThiCongSerializer
from accounts.permissions import IsAdmin

class LichThiCongView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = LichThiCong.objects.all()
    serializer_class = LichThiCongSerializer
    lookup_field = "malichthicong"