from django.db import models


class Timduong(models.Model):
    objectid = models.IntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
    maduong = models.CharField(db_column='MaDuong', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenduong = models.CharField(db_column='TenDuong', max_length=500, blank=True, null=True)  # Field name made lowercase.
    shape = models.TextField(db_column='SHAPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TIMDUONG'
