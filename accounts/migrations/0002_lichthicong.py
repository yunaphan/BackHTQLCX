# Generated by Django 2.1 on 2019-11-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LichThiCong',
            fields=[
                ('malichthicong', models.AutoField(primary_key=True, serialize=False)),
                ('tenlichthicong', models.CharField(max_length=100)),
                ('NgayBD', models.DateField()),
                ('NgayHoanThanh', models.DateField()),
                ('ghichu', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
