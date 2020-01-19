from django.contrib import admin

from . import models

class tesA(admin.ModelAdmin):
    list_display=('nama','email','deskripsi','tanggal_kirim')
    readonly_fields = ['tanggal_kirim']
    list_filter=('tanggal_kirim','email')

admin.site.register(models.testi,tesA)
admin.site.site_header = "Toko Sinar Mas"
