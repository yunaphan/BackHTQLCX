from rest_framework import serializers
from accounts.models import ChiTietThiCong

class ChiTietLichThiCongSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChiTietThiCong
        fields = ('macttc', 'objectid', 'taikhoan', 'trangthaitc', 'lichthicong', 'ghichu', 'hinhthucthicong', 'ngaycapnhat')