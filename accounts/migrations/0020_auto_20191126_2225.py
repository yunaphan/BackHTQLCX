# Generated by Django 2.1 on 2019-11-26 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20191125_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chucnangnguoidung',
            name='machucnang',
        ),
        migrations.RemoveField(
            model_name='chucnangnguoidung',
            name='maquyen',
        ),
        migrations.DeleteModel(
            name='Chucnang',
        ),
        migrations.DeleteModel(
            name='Quyennguoidung',
        ),
    ]
