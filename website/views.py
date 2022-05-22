from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render
from website.models import *

# Create your views here.
def home(request):
    return render(request,"inde.html")

def products(request):
    garmets = product.objects.all().filter(category="garmets")[:10]
    lights = product.objects.all().filter(category="lights")[:10]
    dere = driver.objects.all().values()
    context={
        "garmets":garmets,
        "lights":lights,
        "dere":dere,
    }
    return render(request,"products.html",context)

def about(request):
    return render(request,"about.html")


def prod(request,ext):
    if ext == "oldest":
        pd = product.objects.all().order_by('-id')

    elif ext == "new":
        pd = product.objects.all().order_by('id')

    else:
        pd = product.objects.all().filter(category=ext)
    
    context={
        "pd":pd,
        "ext":ext,
    }
    return render(request,"each.html",context)

def garmets(request):
    garmets = product.objects.all().filter(category="Garmets")
    lst=[]
    for i in garmets:
        lst.append([i.name,i.category,i.description,i.price,i.seller,i.available,i.date,i.negotiable,
        i.photo])

    print(garmets)
    print(lst)
    context={
        "lst":lst,
    }
    return render(request,"garmets.html",context)

def lights(request):
    lights = product.objects.all().filter(category="Electronic")
    lst = []
    for i in lights:
        lst.append([i.name,i.category,i.description,i.price,i.seller,i.available,i.date,i.negotiable,
        i.photo])
   
    print(lst)
    context={
        "lst":lst,
    }
    if request.method == "post":
        results = product.objects.filter(name__contains=request.POST["search"])
        context['results'] = results
        return render(request,"search.html")
    return render(request,"lights.html",context)

def search(request):
    pass