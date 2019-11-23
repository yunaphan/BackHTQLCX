from rest_framework import serializers
from accounts.Models.HinhThucThiCongModel import Hinhthucthicong
from accounts.Serializers.LichThiCongSerializer import LichThiCongSerializer

class HinhThucThiCongSeria(serializers.ModelSerializer):
    maloai = serializers.CharField(max_length=10, required=True)
    tenloai = serializers.CharField(max_length=50, required=True)
    lichthicong = LichThiCongSerializer(many=True, read_only=True)

    class Meta:
        model = Hinhthucthicong
        fields = ('maloai', 'tenloai', 'lichthicong')

    def create(self, validated_data):
        return Hinhthucthicong.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.maloai = validated_data.get('maloai', instance.maloai)
        instance.tenloai = validated_data.get('tenloai', instance.tenloai)
        # instance.lichthicong = validated_data.get('lichthicong', instance.lichthicong)
        instance.save()
        return instance