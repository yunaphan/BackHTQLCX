from rest_framework import serializers
from accounts import models
from django.db import connections

class TrangThaiThiCongSerializer(serializers.ModelSerializer):
    matrangthaitc = serializers.IntegerField()
    trangthaitc = serializers.CharField(max_length=50, required=True)
    ghichu = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)

    class Meta:
        model = models.Trangthaitc
        fields = ('matrangthaitc', 'trangthaitc', 'ghichu')
    #
    # def create(self, validated_data):
    #     trangthaitc = connections.cursor()
    #
    #     return models.Trangthaitc.objects.using('DoThi').create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.matrangthaitc = validated_data.get('matrangthaitc', instance.matrangthaitc)
    #     instance.trangthaitc = validated_data.get('trangthaitc', instance.trangthaitc)
    #     instance.ghichu = validated_data.get('ghichu', instance.ghichu)
    #     instance.save()
    #     return instance