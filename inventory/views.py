from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from inventory.models import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,"index.html")
    else:
        return redirect("/sign")

@login_required
def stocks(request):
    stock = stockModel.objects.all().values()
    context={
        "stock":stock,
        "id":id,
        "save":False,
    }
    print(context["save"])
    if request.method == "POST":
        name = request.POST["name"]
        quantity =request.POST["quantity"]
        buying = request.POST["buying"]
        selling = request.POST["selling"]
        date = request.POST["date"]
        new = stockModel.objects.create(name=name,quantity=quantity,buying=buying,selling=selling,date=date)
        new.save()
        context["save"] = True
        print(context)
    
    return render(request,'stocks.html',context)

@login_required
def order(request):
    orders = orderModel.objects.all().values()

    context={
        "orders":orders,
    }
    return render(request,"order.html",context)

@login_required
def users(request):
    return render(request,"users.html")

@login_required
def edit(request,id):
    stock = stockModel.objects.filter(id=id)
    print(stock)
    lst = []
    for i in stock:
        lst.append([i.id,i.name,i.quantity,i.selling,i.date])
    if request.method == "POST":
        name = request.POST["name"]
        stockModel.objects.get(id=id)
    
    context = {
        "lst":lst,
    }
    return render(request,"edit_stock.html",context)

def log_out(request):
    logout(request)
    return redirect("/home")

def sign(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("authenticated")
            return redirect("/home")
        else:
            print("did not log")
    return render(request,"sign.html")

