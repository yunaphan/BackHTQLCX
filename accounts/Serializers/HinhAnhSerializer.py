from rest_framework import serializers
from accounts.Models.HinhAnhCXModel import Hinhanhcayxanh
from django.db import connections

class HinhAnhCayXanhSerializer(serializers.Serializer):
    maanh = serializers.IntegerField()
    mota = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    duongdanhinhanh = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    objectid = serializers.IntegerField()

    class Meta:
        model = Hinhanhcayxanh
        fields = "__all__"

    def create(self, validated_data):
        objectid = validated_data['objectid']
        duongdanhinhanh = validated_data['duongdanhinhanh']
        mota = validated_data['mota']
        ref = connections['DoThi'].cursor()
        return ref.execute("insert into HINHANHCAYXANH values (%s, %s, %s)", [objectid, duongdanhinhanh, mota])

    def update(self, instance, validated_data):
        instance.objectid = validated_data.get('objectid', instance.objectid)
        instance.duongdanhinhanh = validated_data.get('duongdanhinhanh', instance.duongdanhinhanh)
        instance.mota = validated_data.get('mota', instance.mota)
        instance.save()
        return instance
