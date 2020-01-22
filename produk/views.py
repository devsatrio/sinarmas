from django.shortcuts import render
from .models import produk
# from kategori_barang.models import barang
from django.core.paginator import Paginator

def index(request):
    data_produk = produk.objects.all().order_by('-id')
    paginator = Paginator(data_produk, 8)
    page = request.GET.get('page')
    data_produk = paginator.get_page(page)

    context = {
        'artikel':data_produk,
    }
    return render(request,'produk/index.html',context)
