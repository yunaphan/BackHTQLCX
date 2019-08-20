from rest_framework import serializers
from accounts.Models.CayXanhModel import Cayxanh

class CayXanhserializer(serializers.ModelSerializer):
    objectid = serializers.IntegerField()
    sohieu = serializers.CharField()
    matencx = serializers.CharField()
    kinhdo = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True)
    vido = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True)
    duongkinh = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True)
    chieucao = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True)
    dorongtan = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True)
    ngaytrong = serializers.DateField()
    ngaycapnhat = serializers.DateField()
    thuoctinh = serializers.CharField()
    ghichu = serializers.CharField()
    matinhtrang = serializers.CharField()
    tuyenduong = serializers.CharField()
    nguoicapnhat = serializers.CharField()

    class Meta:
        model = Cayxanh
        fields = ('objectid', 'sohieu', 'matencx', 'kinhdo', 'vido', 'duongkinh',
                  'chieucao', 'dorongtan', 'ngaytrong', 'ngaycapnhat', 'thuoctinh',
                  'ghichu', 'matinhtrang', 'tuyenduong', 'nguoicapnhat' )