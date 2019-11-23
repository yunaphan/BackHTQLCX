# Generated by Django 2.1 on 2019-11-23 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20191123_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chucnangnguoidung',
            name='machucnang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chuc_nang_nguoi_dung', to='accounts.Chucnang'),
        ),
        migrations.AlterField(
            model_name='chucnangnguoidung',
            name='maquyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quyen_nguoi_dung', to='accounts.Quyennguoidung'),
        ),
    ]
