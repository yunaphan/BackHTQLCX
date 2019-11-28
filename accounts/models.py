from django.db import models
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from accounts.Models.CayXanhModel import Cayxanh
from accounts.Models.HinhThucThiCongModel import Hinhthucthicong
from accounts.Models.TimDuongModel import Timduong
from datetime import datetime
from django.core.validators import RegexValidator

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, password, **extra_fields):
        if not email:
            raise ValueError('Tài khoản phải có địa chỉ email')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            ngaysinh=ngaysinh,
            diachi=diachi,
            gioitinh=gioitinh,
            phone=phone,
            firstname=firstname,
            lastname=lastname,
            # is_employee=is_employee,
            # is_manager=is_manager,
            **extra_fields
        )
        extra_fields.setdefault('is_active', True)
        # extra_fields.setdefault('is_employee', False)
        # extra_fields.setdefault('is_manager', False)
        extra_fields.setdefault('is_admin', False)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_employee(self, username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, password, **extra_fields):
    #     extra_fields.setdefault('is_active', True)
    #     extra_fields.setdefault('is_employee', True)
    #     extra_fields.setdefault('is_manager', False)
    #     extra_fields.setdefault('is_admin', False)
    #     return self.create_user(
    #         username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, password=password, **extra_fields)
    #
    # def create_manager(self, username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, password, **extra_fields):
    #     extra_fields.setdefault('is_active', True)
    #     extra_fields.setdefault('is_employee', False)
    #     extra_fields.setdefault('is_manager', True)
    #     extra_fields.setdefault('is_admin', False)
    #     return self.create_user(
    #         username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, password=password, **extra_fields)

    def create_superuser(self, username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        # extra_fields.setdefault('is_employee', False)
        # extra_fields.setdefault('is_manager', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(
            username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, password=password, **extra_fields)

class NhomThiCong(models.Model):
    manhomthicong = models.AutoField(primary_key=True)
    tennhomthicong = models.CharField(max_length=100)
    # nhomtruong = models.BooleanField(default=False)

    def __str__(self):
        return self.tennhomthicong

class Quyennguoidung(models.Model):
    maquyen = models.IntegerField(primary_key=True)
    quyennguoidung = models.CharField(max_length=100)

    def __str__(self):
        return self.quyennguoidung

class MyUser(AbstractBaseUser):
    username = models.CharField(
                    max_length=300,
                    validators=[
                        RegexValidator(regex=USERNAME_REGEX,
                                        message="Tên biến không hợp lệ",
                                        code='invalid_username'
                                )],
                    unique=True
                )
    # password = models.CharField('password', max_length=128)
    email = models.EmailField(
                max_length=255,
                unique=True,
                verbose_name='email address'
        )
    is_admin = models.BooleanField(default=False)
    # is_manager = models.BooleanField(default=False)
    # is_employee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    gioitinh = models.CharField(max_length=10, null=True)
    ngaysinh = models.DateField(null=True)
    diachi = models.CharField(max_length=300, null=True)
    noti_token = models.CharField(max_length=300, null=True)
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    middlename = models.CharField(max_length=255, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    duongdanavatar = models.FileField(upload_to='avatar', blank=True, null=True)
    phone = models.CharField(max_length=10, null=True)
    nhomthicong = models.ForeignKey(NhomThiCong, on_delete=models.DO_NOTHING, related_name="thanhviennhomthicong", null=True, blank=True)
    quyen = models.ForeignKey(Quyennguoidung, on_delete=models.CASCADE, related_name="quyen", null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'ngaysinh', 'gioitinh', 'diachi',
                       'is_admin', 'is_active', 'phone', 'firstname', 'lastname', 'duongdanavatar', ]

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, object=None):
        return True

    def has_perms(self, perm, object=None):
        return True

    def has_module_perms(self, app_lable):
        return True

class Trangthaitc(models.Model):
    matrangthaitc = models.IntegerField(primary_key=True)
    trangthaitc = models.CharField(max_length=100)
    ghichu = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.trangthaitc

# class NgayThiCong(models.Model):
#     mangaytc = models.AutoField(primary_key=True)
#     NgayBD = models.DateField(auto_now=True)
#     NgayHoanThanh = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return "%s - %s" % (self.NgayBD, self.NgayHoanThanh)

# class LichThiCong(models.Model):
#     malichthicong = models.AutoField(primary_key=True)
#     tenlichthicong = models.CharField(max_length=100)
#     ghichu = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.tenlichthicong

class ChiTietThiCong(models.Model):
    macttc = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tuyenduong = models.CharField(max_length=100)
    nhomthiconglich = models.ForeignKey(NhomThiCong, related_name="nhomthiconglich", on_delete=models.DO_NOTHING, null=True, blank=True)
    lichthicong = models.CharField(max_length=100)
    hinhthucthicong = models.ForeignKey(Hinhthucthicong, related_name="lichthicong", on_delete=models.DO_NOTHING,
                                        null=True, blank=True)
    trangthaitc = models.ForeignKey(Trangthaitc, related_name="trangthailichthicong", on_delete=models.DO_NOTHING,
                                    null=True, blank=True)
    mota = models.CharField(max_length=255, null=True, blank=True)
    NgayBD = models.DateField()
    NgayHoanThanh = models.DateField()
    ngaycapnhat = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.lichthicong

class Chucnang(models.Model):
    machucnang = models.IntegerField(primary_key=True)
    chucnang = models.CharField(max_length=100)

    def __str__(self):
        return self.chucnang

class Chucnangnguoidung(models.Model):
    machucnangnguoidung = models.AutoField(primary_key=True)
    maquyen = models.ForeignKey(Quyennguoidung, on_delete=models.CASCADE, related_name="quyen_nguoi_dung", null=True, blank=True)
    machucnang = models.ForeignKey(Chucnang, on_delete=models.CASCADE, related_name="chuc_nang_nguoi_dung", null=True, blank=True)
    xem = models.CharField(max_length=100, null=True, blank=True)
    them = models.CharField(max_length=100, null=True, blank=True)
    sua = models.CharField(max_length=100, null=True, blank=True)
    xoa = models.CharField(max_length=100, null=True, blank=True)
    xuat = models.CharField(max_length=100, null=True, blank=True)

class Hinhanhcayxanh(models.Model):
    maanh = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    duongdanhinhanh = models.TextField(blank=True, null=True)
    mota = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HINHANHCAYXANH'

