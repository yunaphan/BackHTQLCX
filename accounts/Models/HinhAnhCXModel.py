from django.db import models


class Hinhanhcayxanh(models.Model):
    maanh = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    duonngdanhinhanh = models.CharField(max_length=100, blank=True, null=True)
    mota = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'HINHANHCAYXANH'

