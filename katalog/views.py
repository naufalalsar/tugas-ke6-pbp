from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_katalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'katalog': data_katalog_item,
        'nama': 'Muhammad Naufal Zaky Alsar',
        'npm' : '2106752041'
        }
    return render(request, "katalog.html", context)