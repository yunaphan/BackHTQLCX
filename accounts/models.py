from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, ngaysinh, diachi, gioitinh, password, **extra_fields):
        if not email:
            raise ValueError('Tài khoản phải có địa chỉ email')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            ngaysinh=ngaysinh,
            diachi=diachi,
            gioitinh=gioitinh,
            **extra_fields
        )
        extra_fields.setdefault('is_active', True)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, ngaysinh, diachi, gioitinh, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(
            username, email, ngaysinh, diachi, gioitinh, password=password, **extra_fields
        )

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
    password = models.CharField('password', max_length=128)
    email = models.EmailField(
                max_length=255,
                unique=True,
                verbose_name='email address'
        )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    gioitinh = models.CharField(max_length=10, null=True)
    ngaysinh = models.DateField(null=True)
    diachi = models.CharField(max_length=300, null=True)
    noti_token = models.CharField(max_length=300, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'ngaysinh', 'gioitinh', 'diachi', 'is_admin', 'is_active']

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