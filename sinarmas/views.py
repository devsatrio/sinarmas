from django.shortcuts import render,HttpResponse
from blog.models import artikel
from kategori_artikel.models import kategori_artikel
from django.core.paginator import Paginator
from produk.models import produk
from testimoni.models import testi

def index(request):
    data_artikel = artikel.objects.all().order_by('-id')[0:3]
    data_produk = produk.objects.all().order_by('-id')[0:5]
    data_testimoni = testi.objects.all().order_by('-id')[0:3]
    context={
        'artikel':data_artikel,
        'produk':data_produk,
        'testimoni':data_testimoni,
    }
    return render(request,'index.html',context)