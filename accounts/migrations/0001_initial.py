# Generated by Django 2.1 on 2019-11-16 16:42

import accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cayxanh',
            fields=[
                ('objectid', models.IntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('sohieu', models.CharField(blank=True, db_column='SoHieu', max_length=50, null=True)),
                ('matencx', models.CharField(db_column='MaTenCX', max_length=50)),
                ('kinhdo', models.DecimalField(blank=True, db_column='KinhDo', decimal_places=10, max_digits=31, null=True)),
                ('vido', models.DecimalField(blank=True, db_column='ViDo', decimal_places=10, max_digits=31, null=True)),
                ('duongkinh', models.DecimalField(blank=True, db_column='DuongKinh', decimal_places=10, max_digits=31, null=True)),
                ('chieucao', models.DecimalField(blank=True, db_column='ChieuCao', decimal_places=10, max_digits=31, null=True)),
                ('dorongtan', models.DecimalField(blank=True, db_column='DoRongTan', decimal_places=10, max_digits=31, null=True)),
                ('ngaytrong', models.DateTimeField(blank=True, db_column='NgayTrong', null=True)),
                ('ngaycapnhat', models.DateTimeField(blank=True, db_column='NgayCapNhat', null=True)),
                ('thuoctinh', models.CharField(blank=True, db_column='ThuocTinh', max_length=50, null=True)),
                ('ghichu', models.CharField(blank=True, db_column='GhiChu', max_length=50, null=True)),
                ('matinhtrang', models.IntegerField(blank=True, db_column='MaTinhTrang', null=True)),
                ('tuyenduong', models.CharField(blank=True, db_column='TuyenDuong', max_length=20, null=True)),
                ('shape', models.TextField(blank=True, db_column='Shape', null=True)),
                ('nvks_x', models.DecimalField(blank=True, db_column='NVKS_X', decimal_places=8, max_digits=38, null=True)),
                ('nvks_y', models.DecimalField(blank=True, db_column='NVKS_Y', decimal_places=8, max_digits=38, null=True)),
                ('nguoicapnhat', models.CharField(blank=True, db_column='NguoiCapNhat', max_length=200, null=True)),
            ],
            options={
                'db_table': 'CAYXANH',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hinhthucthicong',
            fields=[
                ('maloai', models.CharField(db_column='MaLoai', max_length=10, primary_key=True, serialize=False)),
                ('tenloai', models.CharField(blank=True, db_column='TenLoai', max_length=50, null=True)),
            ],
            options={
                'db_table': 'HinhThucThiCong',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Phuongxa',
            fields=[
                ('objectid', models.IntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('tenphuongxa', models.CharField(blank=True, db_column='TenPhuongXa', max_length=254, null=True)),
                ('maquanhuyen', models.CharField(blank=True, db_column='MaQuanHuyen', max_length=20, null=True)),
                ('maphuongxa', models.CharField(blank=True, db_column='MaPhuongXa', max_length=20, null=True)),
                ('loai', models.CharField(blank=True, db_column='Loai', max_length=20, null=True)),
                ('tenkhongdau', models.CharField(blank=True, db_column='TenKhongDau', max_length=50, null=True)),
                ('shape', models.TextField(blank=True, db_column='Shape', null=True)),
            ],
            options={
                'db_table': 'PHUONGXA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quanhuyen',
            fields=[
                ('objectid', models.IntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('maquanhuyen', models.CharField(blank=True, db_column='MaQuanHuyen', max_length=20, null=True)),
                ('tenquanhuyen', models.CharField(blank=True, db_column='TenQuanHuyen', max_length=20, null=True)),
                ('matinh', models.CharField(blank=True, db_column='MaTinh', max_length=12, null=True)),
                ('loai', models.CharField(blank=True, db_column='Loai', max_length=20, null=True)),
                ('tenkhongdau', models.CharField(blank=True, db_column='TenKhongDau', max_length=20, null=True)),
                ('shape', models.TextField(blank=True, db_column='Shape', null=True)),
            ],
            options={
                'db_table': 'QUANHUYEN',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tencx',
            fields=[
                ('matencx', models.CharField(db_column='MaTenCX', max_length=10, primary_key=True, serialize=False)),
                ('tencx', models.CharField(blank=True, db_column='TenCX', max_length=50, null=True)),
            ],
            options={
                'db_table': 'TenCX',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Timduong',
            fields=[
                ('objectid', models.IntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('maduong', models.CharField(blank=True, db_column='MaDuong', max_length=50, null=True)),
                ('tenduong', models.CharField(blank=True, db_column='TenDuong', max_length=500, null=True)),
                ('shape', models.TextField(blank=True, db_column='SHAPE', null=True)),
            ],
            options={
                'db_table': 'TIMDUONG',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trangthaicx',
            fields=[
                ('matinhtrang', models.IntegerField(db_column='MaTinhTrang', primary_key=True, serialize=False)),
                ('tinhtrang', models.CharField(blank=True, db_column='TinhTrang', max_length=255, null=True)),
                ('ghichu', models.TextField(blank=True, db_column='GhiChu', null=True)),
            ],
            options={
                'db_table': 'TrangThaiCX',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=300, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Tên biến không hợp lệ', regex='^[a-zA-Z0-9.+-]*$')])),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('gioitinh', models.CharField(max_length=10, null=True)),
                ('ngaysinh', models.DateField(null=True)),
                ('diachi', models.CharField(max_length=300, null=True)),
                ('noti_token', models.CharField(max_length=300, null=True)),
                ('firstname', models.CharField(max_length=255, null=True)),
                ('lastname', models.CharField(max_length=255, null=True)),
                ('middlename', models.CharField(max_length=255, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('duongdanavatar', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('phone', models.CharField(max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hinhanhcayxanh',
            fields=[
                ('maanh', models.AutoField(db_column='maanh', primary_key=True, serialize=False)),
                ('objectid', models.IntegerField(db_column='objectid')),
                ('duongdanhinhanh', models.ImageField(upload_to="CayXanh", blank=True, null=True)),
                ('mota', models.TextField(blank=True, db_column='mota', null=True)),
            ],
            options={
                'db_table': 'HINHANHCAYXANH',
                'managed': False,
            },
        ),
    ]
