from rest_framework import serializers
from accounts.Models.TimDuongModel import Timduong
from accounts.Serializers.ChiTietLichThiCongSerializer import ChiTietLichThiCongSerializer

class DuongSeria(serializers.ModelSerializer):
    objectid = serializers.IntegerField()
    maduong = serializers.CharField(max_length=50)
    tenduong = serializers.CharField(max_length=500)
    tuyenduongthicong = ChiTietLichThiCongSerializer(many=True, read_only=True)

    class Meta:
        model = Timduong
        fields =('objectid', 'maduong', 'tenduong', 'tuyenduongthicong')