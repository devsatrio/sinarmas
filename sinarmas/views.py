from django.shortcuts import render,HttpResponse

def index(request):
    context={
        'head':'halo',
    }
    return render(request,'index.html',context)