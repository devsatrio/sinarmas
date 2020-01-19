from django.db import models

# Create your models here.

class kategori_artikel(models.Model):
    nama_kategori = models.CharField(max_length=35)
    tanggal_buat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_kategori

