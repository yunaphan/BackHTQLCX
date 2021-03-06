# Generated by Django 2.1 on 2019-11-28 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20191126_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lichthicong',
            name='NgayBD',
        ),
        migrations.RemoveField(
            model_name='lichthicong',
            name='NgayHoanThanh',
        ),
        migrations.RemoveField(
            model_name='lichthicong',
            name='hinhthucthicong',
        ),
        migrations.RemoveField(
            model_name='lichthicong',
            name='trangthaitc',
        ),
        migrations.AddField(
            model_name='chitietthicong',
            name='NgayBD',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='chitietthicong',
            name='NgayHoanThanh',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='chitietthicong',
            name='hinhthucthicong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lichthicong', to='accounts.Hinhthucthicong'),
        ),
        migrations.AddField(
            model_name='chitietthicong',
            name='trangthaitc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trangthailichthicong', to='accounts.Trangthaitc'),
        ),
    ]
