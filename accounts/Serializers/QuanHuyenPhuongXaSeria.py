from rest_framework import serializers
from accounts.Models.QuanHuyenPhuongXaModel import Quanhuyen, Phuongxa

class QuanHuyenSeria(serializers.ModelSerializer):
    objectid = serializers.IntegerField()
    maquanhuyen = serializers.CharField(max_length=20)
    tenquanhuyen = serializers.CharField(max_length=20)
    matinh = serializers.CharField(max_length=12)
    loai = serializers.CharField(max_length=20)
    tenkhongdau = serializers.CharField(max_length=20)

    class Meta:
        model = Quanhuyen
        fields = ('objectid', 'maquanhuyen', 'tenquanhuyen', 'matinh', 'loai', 'tenkhongdau')

class PhuongXaSeria(serializers.ModelSerializer):
    objectid = serializers.IntegerField()
    maquanhuyen = serializers.CharField(max_length=20)
    maphuongxa = serializers.CharField(max_length=20)
    tenphuongxa = serializers.CharField(max_length=12)
    loai = serializers.CharField(max_length=20)
    tenkhongdau = serializers.CharField(max_length=20)

    class Meta:
        model = Phuongxa
        fields = ('objectid', 'maquanhuyen', 'maphuongxa', 'tenphuongxa', 'loai', 'tenkhongdau')