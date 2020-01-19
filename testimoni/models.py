from django.db import models

class testi(models.Model):
    nama = models.CharField(max_length=40)
    email = models.EmailField()
    deskripsi = models.TextField()
    tanggal_kirim = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.nama
