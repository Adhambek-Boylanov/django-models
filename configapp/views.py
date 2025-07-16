from django.shortcuts import render
from django.http import HttpResponse
from .models import Tuman,Viloyat,Mahalla
# def index(request):
#     tums = Tuman.objects.all()
#     vil = Viloyat.objects.all()
#     mah = Mahalla.objects.all()
#     s = {
#         "tums":tums,
#         "title":"MAHALLALAR",
#         "vil":vil,
#         "title1":"VILOYATLAR",
#         "mah":mah,
#         "title2":"MAHALLALAR"
#     }
#     return render(request,'index1.html',context=s)







def index1(request):
    s = "<h1> TUMANLAR </h1> \n"
    tums = Tuman.objects.all()
    for i in tums:
        s += f"<p> Title: {i.title} --> Context: {i.context} </p> <hr> \n"
    s += "<h1> VILOYATLAR </h1> \n"
    vil = Viloyat.objects.all()
    for item in vil:
        s += f"<p> Viloyat: {item.title} --> Context: {item.context} </p> <hr> \n"
    s += "<h1> MAHALLALAR </h1> \n"
    mah = Mahalla.objects.all()
    for it in mah:
        s+= f"<p> Mahalla: {it.title} --> Context: {it.context} </p> <hr> \n"
    return HttpResponse(s)











# Create your views here.
