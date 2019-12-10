from accounts.Models.TrangThaiCXModel import Trangthaicx
from django.db import models


class Cayxanh(models.Model):
    objectid = models.IntegerField(db_column='OBJECTID', primary_key=True)
    sohieu = models.CharField(db_column='SoHieu', max_length=50, blank=True, null=True)
    matencx = models.CharField(db_column='MaTenCX', max_length=50)
    kinhdo = models.DecimalField(db_column='KinhDo', max_digits=31, decimal_places=10, blank=True, null=True)
    vido = models.DecimalField(db_column='ViDo', max_digits=31, decimal_places=10, blank=True, null=True)
    duongkinh = models.DecimalField(db_column='DuongKinh', max_digits=31, decimal_places=10, blank=True, null=True)
    chieucao = models.DecimalField(db_column='ChieuCao', max_digits=31, decimal_places=10, blank=True, null=True)
    dorongtan = models.DecimalField(db_column='DoRongTan', max_digits=31, decimal_places=10, blank=True, null=True)
    ngaytrong = models.DateTimeField(db_column='NgayTrong', blank=True, null=True)
    ngaycapnhat = models.DateTimeField(db_column='NgayCapNhat', blank=True, null=True)
    thuoctinh = models.CharField(db_column='ThuocTinh', max_length=50, blank=True, null=True)
    ghichu = models.CharField(db_column='GhiChu', max_length=50, blank=True, null=True)
    matinhtrang = models.IntegerField(db_column='MaTinhTrang', blank=True, null=True)
    tuyenduong = models.CharField(db_column='TuyenDuong', max_length=20, blank=True, null=True)
    phuongxa = models.CharField(db_column='PhuongXa', max_length=50, blank=True, null=True)
    quanhuyen = models.CharField(db_column='QuanHuyen', max_length=50, blank=True, null=True)
    shape = models.TextField(db_column='Shape', blank=True, null=True)
    nvks_x = models.DecimalField(db_column='NVKS_X', max_digits=38, decimal_places=8, blank=True, null=True)
    nvks_y = models.DecimalField(db_column='NVKS_Y', max_digits=38, decimal_places=8, blank=True, null=True)
    nguoicapnhat = models.CharField(db_column='NguoiCapNhat', max_length=200, blank=True, null=True)
    # xoabo = models.CharField(db_column='Xoabo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAYXANH'

    def __str__(self):
        return '%d: %s' % (self.objectid, self.sohieu)
