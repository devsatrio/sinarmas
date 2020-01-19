from django.db import models

class barang(models.Model): 
	nama_kategori = models.CharField(max_length=30)
	tanggal = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.nama_kategori