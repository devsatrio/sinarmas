from django.shortcuts import render
from .models import testi

def index(request):
    # data_testi = testi.objects.all()
    data_testi = testi.objects.all().order_by('-id')
    # data_testi = testi.objects.all().order_by('-id')[0:3]
    # data_testi = testi.objects.all().filter(nama='nanang')
    # data_testi = testi.objects.all().get(nama='nanang')

    context = {
        'testi':data_testi,
    }
    return render(request,'testimoni/index.html',context)
