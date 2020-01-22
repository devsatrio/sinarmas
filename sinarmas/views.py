from django.shortcuts import render,HttpResponse
from blog.models import artikel
from kategori_artikel.models import kategori_artikel
from django.core.paginator import Paginator

def index(request):
    data_kategori = kategori_artikel.objects.all()
    data_artikel = artikel.objects.all().order_by('-id')
    paginator = Paginator (data_artikel, 3)
    page = request.GET.get('page')
    data_artikel = paginator.get_page(page)
    
    context={
        'head':'halo',
        'kategori':data_kategori,
        'artikel':data_artikel,
    }
    return render(request,'index.html',context)