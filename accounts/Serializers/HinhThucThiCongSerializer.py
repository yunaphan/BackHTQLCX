from rest_framework import serializers
from accounts.Models.HinhThucThiCongModel import Hinhthucthicong

class HinhThucThiCongSeria(serializers.ModelSerializer):
    maloai = serializers.CharField(max_length=10, required=True)
    tenloai = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = Hinhthucthicong
        fields = ('maloai', 'tenloai')

    def create(self, validated_data):
        return Hinhthucthicong.objects.using('DoThi').create(**validated_data)

    def update(self, instance, validated_data):
        instance.maloai = validated_data.get('maloai', instance.maloai)
        instance.tenloai = validated_data.get('tenloai', instance.tenloai)
        instance.save()
        return instance