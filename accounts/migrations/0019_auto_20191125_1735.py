# Generated by Django 2.1 on 2019-11-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20191125_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitietthicong',
            name='tuyenduong',
            field=models.CharField(max_length=100),
        ),
    ]
