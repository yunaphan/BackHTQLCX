from rest_framework import serializers
from accounts.Models.CayXanhModel import Cayxanh
from accounts.Serializers.ChiTietLichThiCongSerializer import ChiTietLichThiCongSerializer

class CayXanhserializer(serializers.ModelSerializer):
    matinhtrang = serializers.StringRelatedField(many=True)
    # ob_cayxanh = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cayxanh
        fields = ('objectid', 'sohieu', 'matencx', 'kinhdo', 'vido', 'duongkinh',
                  'chieucao', 'dorongtan', 'ngaytrong', 'ngaycapnhat', 'thuoctinh',
                  'ghichu', 'matinhtrang', 'tuyenduong', 'nguoicapnhat')