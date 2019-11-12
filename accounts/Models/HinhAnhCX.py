from django.db import models
from accounts.Models.CayXanhModel import Cayxanh

class Hinhanh(models.Model):
    maanh = models.AutoField(db_column='idAnh', primary_key=True)
    tenanh = models.CharField(db_column='TenAnh', max_length=255)
    mota = models.CharField(db_column='MoTa', max_length=255, blank=True, null=True)
    duongdan = models.TextField(db_column='DuongDan', blank=True, null=True)
    objectid = models.IntegerField(db_column='objectid')

    class Meta:
        managed = False
        db_table = 'HinhAnh'
