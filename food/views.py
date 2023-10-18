from django.shortcuts import render
from food.models import TestTable
from food.models import TestTable1

# Create your views here.
def web2(request):
    if request.method=="POST":
       name2=request.POST.get('name2')
       email2=request.POST.get('email2')
       phone2=request.POST.get('phone2')
       web2=TestTable(name2=name2,email2=email2,phone2=phone2)
       web2.save()
    return render(request,"web2.html")

def zomato(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        date=request.POST.get('date')
        email=request.POST.get('email')
        number=request.POST.get('number')
        food1=request.POST.get('food1')
        restaurant=request.POST.get('restaurant')
        drinks=request.POST.get('drinks')
        soups=request.POST.get('soups')
        dishes=request.POST.get('dishes')
        order=request.POST.get('order')
        zomato=TestTable1(uname=uname,date=date,email=email,number=number,food1=food1,restaurant=restaurant,drinks=drinks,soups=soups,dishes=dishes,order=order)
        zomato.save()
    return render(request,"zomato.html")





