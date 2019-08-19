from rest_framework import serializers
from accounts.Models.CayXanhModel import Cayxanh

class CayXanhSerializer(serializers.ModelSerializer):

    class Meta:
        model = "Cayxanh"
        fields = ('objectid', 'sohieu', 'matencx', 'kinhdo', 'vido', 'duongkinh',
                  'chieucao', 'dorongtan', 'ngaytrong', 'ngaycapnhat', 'thuoctinh',
                  'ghichu', 'matinhtrang', 'tuyenduong', 'nguoicapnhat' )