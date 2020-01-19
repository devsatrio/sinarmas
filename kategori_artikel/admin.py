from django.contrib import admin

from . import models

class kategori_artikel_adm(admin.ModelAdmin):
    list_display = ('nama_kategori','tanggal_buat')

    readonly_fields = ['tanggal_buat']
    
    list_filter = ('tanggal_buat',)

admin.site.register(models.kategori_artikel,kategori_artikel_adm)
admin.site.site_header = "Toko Sinar Mas"


