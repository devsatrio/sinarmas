from django.contrib import admin
from .models import produk

class tampilan(admin.ModelAdmin):
	list_display=('nama_produk','harga','deskripsi','kategori_barang','gambar','tanggal')
	readonly_fields=['tanggal']

admin.site.register(produk,tampilan)