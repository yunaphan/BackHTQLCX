# Generated by Django 2.1 on 2019-11-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_chitietthicong_objectid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitietthicong',
            name='objectid',
            field=models.IntegerField(),
        ),
    ]
