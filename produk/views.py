from django.shortcuts import render
from kategori_barang.models import barang
from .models import produk
from django.core.paginator import Paginator

def index(request):
    data_produk = produk.objects.all().order_by('-id')
    paginator = Paginator(data_produk, 4)
    page = request.GET.get('page')
    data_produk = paginator.get_page(page)

    data_kategori = barang.objects.all().order_by('-id')

    context = {
        'produk':data_produk,
        'kategori':data_kategori,
    }
    return render(request,'produk/index.html',context)

def show(request,barang):
    data_produk = produk.objects.get(slug=barang)
    context = {
        'produk':data_produk,
    }
    return render(request,'produk/show.html',context)
