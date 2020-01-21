from django.contrib import admin
from . models import artikel
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BlogResource(resources.ModelResource):

    class Meta:
        model = artikel
        fields = ('judul','isi')

class PostAdmin(ImportExportModelAdmin):
    resource_class = BlogResource
    readonly_fields = ['slug','tanggal']
    list_display = ['judul','isi','tanggal','gambar','kategori']
    list_filter = ['tanggal','kategori']
    
    
admin.site.register(artikel,PostAdmin)