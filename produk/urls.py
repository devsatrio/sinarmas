from django.urls import path
from . import views

app_name='produk'
urlpatterns=[
	path('<slug:barang>',views.show,name='show'),
	path('',views.index,name='index'),
]