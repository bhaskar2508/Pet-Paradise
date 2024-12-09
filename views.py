from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from.models import CatFood,CatFoodCart,CatHealthCart,CatHealth,CatToys,CatToysCart,DogFood,DogFoodCart,DogHealth,DogHealthCart,DogToys,DogToysCart,Order
from django.http import JsonResponse
import razorpay
from django.http import HttpResponse
from decimal import Decimal

def home(request):
    return render(request,'home.html')


def register_view(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid(): 
            f.save()  
            messages.success(request, 'Registration completed successfully! Please log in.')            
            return redirect('login') 
    else:
        f = UserCreationForm()  
    context = {'form': f}
    return render(request, 'register.html', context)

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            login(request,user)
            request.session['uid'] = user.id
            messages.success(request, ' Please log in.')            
            return redirect('/')
        else:
            messages.error(request, 'Incorrect username or password.')  
            f=LoginForm
            context={'form':f}
            return render(request,'login.html',context)
    else:
        f=LoginForm
        context={'form':f}
        return render(request,'login.html',context)
    

def logout_view(request):
    logout(request)
    return redirect('/')


def store_view(request):
    return render(request,'store.html')

def cart_view(request):
    uid = request.session.get('uid')
    if not uid:
        return redirect('login')  

    try:
        user = User.objects.get(id=uid)
    except User.DoesNotExist:
        return redirect('login')  

    cf = CatFoodCart.objects.filter(user=user) 
    ch = CatHealthCart.objects.filter(user=user) 
    ct = CatToysCart.objects.filter(user=user)
    df=DogFoodCart.objects.filter(user=user)
    dt=DogToysCart.objects.filter(user=user)
    dh=DogHealthCart.objects.filter(user=user)
    context = {
        'cf': cf,
        'ch': ch,
        'ct': ct,  
        'df':df,
        'dt':dt,
        'dh':dh,
    }
    return render(request, 'cart-view.html', context)



def add_to_cart(request,pid):
    catfood=CatFood.objects.get(id=pid)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=CatFoodCart()
    c.catfood=catfood
    c.user=user
    c.save()
    return redirect('/cart')


def cat_food(request): 
    if request.method=='POST':
        f=CatFood(request.POST,request.FILES)
        if f.is_valid():
            f.save()
    cf=CatFood.objects.all()
    context={'cf':cf}
    return render(request,'cat-food.html',context)

def delete(request):
    eid=request.GET.get('id')
    cf=CatFoodCart.objects.get(id=eid)
    cf.delete()
    return redirect('/cart')


def toys(request):
    if request.method=='POST':
        f=CatFood(request.POST,request.FILES)
        if f.is_valid():
            f.save()
    ct=CatToys.objects.all()
    context={'ct':ct}
    return render(request,'cat-toys.html',context)

def cat_toy_cart(request,cit):
    cattoys=CatToys.objects.get(id=cit)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=CatToysCart()
    c.cattoys=cattoys
    c.user=user
    c.save()
    return redirect('/cart')

def delete_cat_toy(request):
    ctd=request.GET.get('id')
    ct=CatToysCart.objects.get(id=ctd)
    ct.delete()
    return redirect('/cart')


def cat_health(request):
    if request.method=='POST':
        f=CatFood(request.POST,request.FILES)
        if f.is_valid():
            f.save()
    ch=CatHealth.objects.all()
    context={'ch':ch}
    return render(request,'cat-health.html',context)

def cat_health_cart(request,chid):
    cathealth=CatHealth.objects.get(id=chid)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=CatHealthCart()
    c.cathealth=cathealth
    c.user=user
    c.save()
    return redirect('/cart')

def delete_cat_health(request):
    hid=request.GET.get('id')
    cf=CatHealthCart.objects.get(id=hid)
    cf.delete()
    return redirect('/cart')

def dog_food(request):
    if request.method=='POST':
        f=DogFood(request.POST,request.FILES)
        if f.is_valid():
            f.save()
    df=DogFood.objects.all()
    context={'df':df}
    return render(request,'dog-food.html',context)


def dog_food_cart(request,dfd):
    dogfood=DogFood.objects.get(id=dfd)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=DogFoodCart()
    c.dogfood=dogfood
    c.user=user
    c.save()
    return redirect('/cart')

def delete_dog_food(request):
    ddf=request.GET.get('id')
    df=DogFoodCart.objects.get(id=ddf)
    df.delete()
    return redirect('/cart')

def dog_toys(request):
    if request.method=='POST':
        f=DogToys(request.POST,request.FILES)
        if f.is_valid():
            f.save()
    dt=DogToys.objects.all()
    context={'dt':dt}
    return render(request,'dog-toys.html',context)

def dog_toys_cart(request,dtd):
    dogtoys=DogToys.objects.get(id=dtd)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=DogToysCart()
    c.dogtoys=dogtoys
    c.user=user
    c.save()
    return redirect('/cart')

def delete_dog_toys(request):
    ddt=request.GET.get('id')
    dt=DogToysCart.objects.get(id=ddt)
    dt.delete()
    return redirect('/cart')


def dog_health(request):
    if request.method=='POST':
        f=DogHealth(request.POST,request.FILES)
        if f.is_valid():
            f.save()
    dh=DogHealth.objects.all()
    context={'dh':dh}
    return render(request,'dog-health.html',context)

def dog_health_cart(request,dhd):
    doghealth=DogHealth.objects.get(id=dhd)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=DogHealthCart()
    c.doghealth=doghealth
    c.user=user
    c.save()
    return redirect('/cart')

def delete_dog_health(request):
    ddh=request.GET.get('id')
    dh=DogHealthCart(id=ddh)
    dh.delete()
    return redirect('/cart')

def pay_now_views(request):
    return render(request,'payment.html')







