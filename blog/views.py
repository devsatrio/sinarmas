from django.shortcuts import render
from .models import artikel
from kategori_artikel.models import kategori_artikel
from django.core.paginator import Paginator

def index(request):
    data_kategori = kategori_artikel.objects.all()
    data_artikel = artikel.objects.all().order_by('-id')
    paginator = Paginator(data_artikel, 3)
    page = request.GET.get('page')
    data_artikel = paginator.get_page(page)

    # parsing data
    context = { 
        'kategori':data_kategori,
        'artikel':data_artikel,
    }
    return render(request,'blog/index.html',context)

def show(request,blogslug):
    detail_artikel = artikel.objects.get(slug=blogslug)
    artikel_lain = artikel.objects.all().order_by('?')[0:3]
    context = {
        'detail_artikel':detail_artikel,
        'artikel_lain':artikel_lain,
    }
    return render(request,'blog/show.html',context)

def bycategori(request,kategori):
    data_kategori = kategori_artikel.objects.all()
    data_artikel = artikel.objects.all().filter(kategori=kategori).order_by('-id')
    paginator = Paginator(data_artikel, 8)
    page = request.GET.get('page')
    data_artikel = paginator.get_page(page)
    detail_kategori = kategori_artikel.objects.get(id=kategori)
    context = {
        'detail_kategori':detail_kategori,
        'kategori':data_kategori,
        'artikel':data_artikel,
    }
    return render(request,'blog/categori.html',context)
