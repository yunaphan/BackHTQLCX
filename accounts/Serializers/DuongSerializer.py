from rest_framework import serializers
from accounts.Models.TimDuongModel import Timduong

class DuongSeria(serializers.ModelSerializer):
    objectid = serializers.IntegerField()
    maduong = serializers.CharField(max_length=50)
    tenduong = serializers.CharField(max_length=500)

    class Meta:
        model = Timduong
        fields =('objectid', 'maduong', 'tenduong')