# from rest_framework import serializers
# from accounts.models import LichThiCong
# from accounts.Serializers.ChiTietLichThiCongSerializer import ChiTietLichThiCongSerializer
#
# class LichThiCongSerializer(serializers.ModelSerializer):
#     chitietlichthicong = ChiTietLichThiCongSerializer(many=True, read_only=True)
#     # tenlichthicong = serializers.CharField(max_length=100, required=False)
#     # NgayHoanThanh = serializers.DateField(required=False, allow_null=True)
#
#     class Meta:
#         model = LichThiCong
#         fields = ('malichthicong', 'tenlichthicong', 'chitietlichthicong', 'ghichu')
