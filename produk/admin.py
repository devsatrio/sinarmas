from django.contrib import admin
from .models import produk
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProdukResource(resources.ModelResource):

	class Meta:
		model = produk
		fields = ('nama_produk','kategori_barang','deskripsi','harga')

class tampilan(ImportExportModelAdmin):
	resource_class = ProdukResource
	readonly_fields = ['slug','tanggal']
	list_display=('nama_produk','harga','deskripsi','kategori_barang','gambar','tanggal')
	readonly_fields=['tanggal']

admin.site.register(produk,tampilan)