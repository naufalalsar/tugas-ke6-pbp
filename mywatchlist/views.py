from django.shortcuts import render
from mywatchlist.models import myWatchList
from django.http import HttpResponse
from django.core import serializers

def show_html(request):
    watchlist = myWatchList.objects.all()

    yes = 0
    no = 0
    
    for movie in watchlist:
        if(movie.watched == "Yes"):
            yes+=1
        else :
            no+=1

    if(yes >= no):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'watchlist': watchlist,
        'nama': 'Muhammad Naufal Zaky Alsar',
        'npm' : '2106752041',
        'message' : message
        
        }
    return render(request, "kinomovies.html", context)

def show_xml(request):

    data = myWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):

    data = myWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")