# Generated by Django 2.1.10 on 2019-07-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190724_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='noti_token',
            field=models.CharField(max_length=300, null=True),
        ),
    ]