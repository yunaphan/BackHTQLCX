from rest_framework import serializers
from accounts.Models.HinhAnhCXModel import Hinhanhcayxanh
from django.db import connections

class HinhAnhCayXanhSerializer(serializers.Serializer):
    mota = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    duongdanhinhanh = serializers.CharField(allow_null=True)
    objectid = serializers.IntegerField()

    class Meta:
        model = Hinhanhcayxanh
        fields = ['mota', 'duongdanhinhanh', 'objectid']

    def create(self, validated_data):
        objectid = validated_data['objectid']
        duongdanhinhanh = validated_data['duongdanhinhanh']
        mota = validated_data['mota']
        ref = connections['DoThi'].cursor()
        return ref.execute("insert into HINHANHCAYXANH values (%s, %s, %s)", [objectid, duongdanhinhanh, mota])
