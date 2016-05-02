from django.db import models
from django.utils import timezone

# Create your models here.
class Alternatif(models.Model):
    kri=models.TextField(null=True,blank=True)
    pp=models.TextField(null=True,blank=True)
    up=models.TextField(null=True,blank=True)
    sp=models.TextField(null=True,blank=True)
    nama_agen=models.TextField(null=True,blank=True)

class Komentar(models.Model):
    nama=models.CharField(max_length=50)
    email=models.EmailField()
    pesan=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
