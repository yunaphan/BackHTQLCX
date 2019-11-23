from rest_framework import serializers
from accounts.models import ChiTietThiCong

class ChiTietLichThiCongSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChiTietThiCong
        fields = "__all__"