# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Timduong(models.Model):
    objectid = models.IntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
    maduong = models.CharField(db_column='MaDuong', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenduong = models.CharField(db_column='TenDuong', max_length=500, blank=True, null=True)  # Field name made lowercase.
    shape = models.TextField(db_column='SHAPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TIMDUONG'
