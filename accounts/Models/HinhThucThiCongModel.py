from django.db import models


class Hinhthucthicong(models.Model):
    maloai = models.CharField(db_column='MaLoai', primary_key=True, max_length=10)  # Field name made lowercase.
    tenloai = models.CharField(db_column='TenLoai', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HinhThucThiCong'

    def __str__(self):
        return self.tenloai
