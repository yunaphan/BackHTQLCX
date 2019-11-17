from django.db import models
from accounts.Models.CayXanhModel import Cayxanh
from accounts.Models.HinhThucThiCongModel import Hinhthucthicong
from accounts.models import MyUser
from accounts.Models.TrangThaiTCModel import Trangthaitc

class CT_THICONGCAYXANH(models.Model):
    macthttc = models.AutoField(primary_key=True)
    objectid = models.ForeignKey(Cayxanh, on_delete=models.CASCADE, related_name='objectid_of_cttc')
    mahttc = models.ForeignKey(Hinhthucthicong, on_delete=models.CASCADE, related_name='httc_of_cttc')
    taikhoan = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='account_cttc')
    matrangthaitc = models.ForeignKey(Trangthaitc, on_delete=models.CASCADE, related_name='status_of_cttc')
    ngayDB = models.DateTimeField(auto_now_add=True)
    NgayHoanThanh = models.DateTimeField(auto_now_add=True)
    NgayKetThuc = models.DateTimeField(auto_now_add=True)