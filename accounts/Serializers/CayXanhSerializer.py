from rest_framework import serializers
from accounts.Models.CayXanhModel import Cayxanh
from accounts.Serializers.ChiTietLichThiCongSerializer import ChiTietLichThiCongSerializer
from accounts.Serializers.HinhAnhSerializer import HinhAnhCayXanhSerializer

class CayXanhserializer(serializers.ModelSerializer):
    # matinhtrang = serializers.StringRelatedField(many=True)
    # ob_cayxanh = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Cayxanh
        fields = ('objectid', 'sohieu', 'matencx', 'matinhtrang', 'kinhdo', 'vido', 'duongkinh',
                  'chieucao', 'dorongtan', 'ngaytrong', 'ngaycapnhat', 'thuoctinh',
                  'ghichu', 'tuyenduong', 'phuongxa', 'quanhuyen', 'nguoicapnhat')