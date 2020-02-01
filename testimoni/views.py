from django.shortcuts import render,redirect
from django.contrib import messages
from .models import testi
from .forms import testimoniform

def index(request):
    # data_testi = testi.objects.all()
    # data_testi = testi.objects.all().order_by('-id')[0:3]
    # data_testi = testi.objects.all().filter(nama='nanang')
    # data_testi = testi.objects.all().get(nama='nanang')
    if request.method == 'POST':
        testi.objects.create(
            nama = request.POST['nama'],
            email = request.POST['email'],
            deskripsi = request.POST['deskripsi'],
        )
        messages.success(request, 'Makasih ya udah kirim umpan balik ke kami :)')
        return redirect('testimoni:index')

    data_testi = testi.objects.all().order_by('-id')
    testi_moniform = testimoniform()
    
    context = {
        'testi':data_testi,
        'testi_moniform':testi_moniform,
    }
    return render(request,'testimoni/index.html',context)
