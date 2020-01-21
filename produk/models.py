from django.db import models
from kategori_barang.models import barang

class produk(models.Model):
	nama_produk = models.CharField(max_length=30)
	harga = models.IntegerField(max_length=50,null=True)
	deskripsi = models.CharField(max_length=50,null=True)
	kategori_barang = models.ForeignKey(barang,on_delete=models.SET_NULL,null=True) 
	gambar = models.ImageField(upload_to='produk_image/',null=True)
	tanggal = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.nama_produk
		
