from django.db import models
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from accounts.Models.CayXanhModel import Cayxanh
from accounts.Models.HinhThucThiCongModel import Hinhthucthicong
from django.core.validators import RegexValidator

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, is_employee, is_manager, password, **extra_fields):
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
            is_employee=is_employee,
            is_manager=is_manager,
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

    def create_superuser(self, username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname, is_employee, is_manager, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        # extra_fields.setdefault('is_employee', False)
        # extra_fields.setdefault('is_manager', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(
            username, email, ngaysinh, diachi, gioitinh, phone, firstname, lastname,  is_employee, is_manager, password=password, **extra_fields)

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
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
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

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'ngaysinh', 'gioitinh', 'diachi',
                       'is_admin', 'is_active', 'is_employee', 'is_manager',
                       'phone', 'firstname', 'lastname', 'duongdanavatar']

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

class LichThiCong(models.Model):
    malichthicong = models.AutoField(primary_key=True)
    tenlichthicong = models.CharField(max_length=100)
    NgayBD = models.DateField()
    NgayHoanThanh = models.DateField()
    ghichu = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.tenlichthicong

class ChiTietThiCong(models.Model):
    macttc = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objectid = models.ForeignKey(Cayxanh, related_name="objectid_cx_cua_thi_cong", on_delete=models.CASCADE)
    taikhoan = models.ForeignKey(MyUser, related_name="nguoi_dung_thi_cong_cong_trinh", on_delete=models.DO_NOTHING)
    trangthaitc = models.ForeignKey(Trangthaitc, related_name="trang_thai_cua_thi_cong", on_delete=models.DO_NOTHING)
    lichthicong = models.ForeignKey(LichThiCong, related_name="lich_thi_cong", on_delete=models.DO_NOTHING)
    ghichu = models.CharField(max_length=255, null=True, blank=True)
    hinhthucthicong = models.ForeignKey(Hinhthucthicong, related_name="hinh_thuc_thi_cong", on_delete=models.DO_NOTHING)
    ngaycapnhat = models.DateField(auto_created=True)
