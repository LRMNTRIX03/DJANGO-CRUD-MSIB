from django.db import models

# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(max_length=50, unique=True)
    harga = models.IntegerField()
    stok = models.IntegerField()
    keterangan = models.TextField()

    def __str__(self):
        return self.nama_barang
