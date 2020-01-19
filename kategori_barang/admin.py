from django.contrib import admin

from . import models

class tampil(admin.ModelAdmin):
	list_display=('nama_kategori','tanggal')
	readonly_fields=['tanggal']

admin.site.register(models.barang,tampil)