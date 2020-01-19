from django.contrib import admin
from .models import artikel

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['judul','isi','tanggal','gambar']
    
admin.site.register(artikel,PostAdmin)