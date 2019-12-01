from rest_framework import serializers
from accounts.Models.TrangThaiCXModel import Trangthaicx

class TrangThaiCXSeria(serializers.ModelSerializer):
    matinhtrang = serializers.IntegerField()
    tinhtrang = serializers.CharField(max_length=255)
    ghichu = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = Trangthaicx
        fields = ('matinhtrang', 'tinhtrang', 'ghichu')

    def create(self, validated_data):
        return Trangthaicx.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.matinhtrang = validated_data.get('MaTinhTrang', instance.matinhtrang)
        instance.tinhtrang = validated_data.get('tinhtrang', instance.tinhtrang)
        instance.ghichu = validated_data.get('ghichu', instance.ghichu)
        instance.save()
        return instance
