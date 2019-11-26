from rest_framework import serializers
from accounts.models import Chucnang, Chucnangnguoidung, Quyennguoidung
from accounts.serializers import UserCreationSerializer


class ChucnangnguoidungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chucnangnguoidung
        fields = "__all__"

class QuyenNguoiDungSerializer(serializers.ModelSerializer):
    quyen_nguoi_dung = ChucnangnguoidungSerializer(many=True, read_only=True)
    quyen = UserCreationSerializer(many=True, read_only=True)

    class Meta:
        model = Quyennguoidung
        fields = "__all__"

class ChucNangSerializer(serializers.ModelSerializer):
    chuc_nang_nguoi_dung = ChucnangnguoidungSerializer(many=True, read_only=True)

    class Meta:
        model = Chucnang
        fields = "__all__"

