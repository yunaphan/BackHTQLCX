from rest_framework import serializers
from accounts.Models.TenCXModel import Tencx

class TenCXSeria(serializers.ModelSerializer):
    matencx = serializers.CharField(max_length=10)
    tencx = serializers.CharField(max_length=50)

    class Meta:
        model = Tencx
        fields = ('matencx', 'tencx')

    def create(self, validated_data):
        return Tencx.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.matencx = validated_data.get('matencx', instance.matencx)
        instance.tencx = validated_data.get('tencx', instance.tencx)
        instance.save()
        return instance