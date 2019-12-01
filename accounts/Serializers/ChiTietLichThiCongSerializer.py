from rest_framework import serializers
from accounts.models import ChiTietThiCong

class ChiTietLichThiCongSerializer(serializers.ModelSerializer):
    trangthaitc = serializers.CharField(max_length=100)

    class Meta:
        model = ChiTietThiCong
        fields = "__all__"