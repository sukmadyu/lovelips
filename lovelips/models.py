from django.db import models
from django.utils import timezone

# Create your models here.
class Alternatif(models.Model):
    kri=models.TextField(null=True,blank=True)
    harga=models.TextField(null=True,blank=True)
    isi=models.TextField(null=True,blank=True)
    pao=models.TextField(null=True,blank=True)
    time=models.TextField(null=True,blank=True)
    cruelty_free=models.TextField(null=True,blank=True)
    nama_product=models.TextField(null=True,blank=True)

class Komentar(models.Model):
    nama=models.CharField(max_length=50)
    email=models.EmailField()
    no_telepon=models.CharField(max_length=12)
    pesan=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
