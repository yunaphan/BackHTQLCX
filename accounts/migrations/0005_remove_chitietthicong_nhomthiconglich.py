# Generated by Django 2.1 on 2019-11-23 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_chitietthicong_nhomthiconglich'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chitietthicong',
            name='nhomthiconglich',
        ),
    ]
