from django.db import models
from django.utils.text import slugify
from kategori_barang.models import barang

class produk(models.Model):
	nama_produk = models.CharField(max_length=30)
	harga = models.IntegerField(null=True)
	deskripsi = models.TextField()
	kategori_barang = models.ForeignKey(barang,on_delete=models.SET_NULL,null=True) 
	gambar = models.ImageField(upload_to='produk_image/',null=True)
	tanggal = models.DateTimeField(auto_now_add=True,null=True)
	slug = models.SlugField(editable=False,blank=True,null=True)

	def save(self):
		self.slug=slugify(self.nama_produk)
		super(produk, self).save()

	def __str__(self):
		return self.nama_produk
