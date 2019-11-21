from rest_framework import serializers
from accounts.models import LichThiCong

class LichThiCongSerializer(serializers.ModelSerializer):

    class Meta:
        model = LichThiCong
        fields = "__all__"
