from django.db import models


class Trangthaicx(models.Model):
    matinhtrang = models.IntegerField(db_column='MaTinhTrang', primary_key=True)  # Field name made lowercase.
    tinhtrang = models.CharField(db_column='TinhTrang', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrangThaiCX'

    def __str__(self):
        return "%d: %s", (self.matinhtrang, self.tinhtrang)
