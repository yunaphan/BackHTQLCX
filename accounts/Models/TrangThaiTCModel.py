from django.db import models

class Trangthaitc(models.Model):
    matrangthai = models.IntegerField(primary_key=True)
    trangthai = models.CharField(max_length=100)