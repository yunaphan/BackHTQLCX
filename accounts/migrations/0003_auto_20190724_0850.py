# Generated by Django 2.1.10 on 2019-07-24 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='diachi',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gioitinh',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='ngaysinh',
            field=models.DateField(null=True),
        ),
    ]