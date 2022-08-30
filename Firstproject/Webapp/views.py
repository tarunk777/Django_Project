from itertools import product
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Webapp.models import (
    Register,
    Contact, 
    Product)
from .forms import ProductForm
from django.shortcuts import redirect
# Create your views here.
def home(request):
    dogs = Product.objects.filter(p_category = 'DOG').order_by('-id')[:3]
    cats = Product.objects.filter(p_category = 'CAT').order_by('-id')[:3]
    fishes = Product.objects.filter(p_category = 'FISH').order_by('-id')[:3]
    data = {
        "dogs":dogs,
        "cats":cats,
        "fishes":fishes}
    if not data:
        return HttpResponse('error')
    return render(request,'index.html',data)

   # return HttpResponse('This is var1 request')
def aboutSection(request):
    return render(request,'About.html')
def serviceSection(request):
    return HttpResponse('This is Services page')
def contactInfo(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        state = request.POST['state']
        city = request.POST['city']
        zip= request.POST['zip']
        query=request.POST['query']
        Contact = Contact(name=name,email=email,state=state,city=city,zip=zip,query=query)
        Contact.save()
        messages.success(request,f"Feedback sent successfully!!")
    return render(request,"Contact.html")


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home/')
        return HttpResponse('Not found or Error')
    return HttpResponse('Error')

def loginPage(request):
        return render(request,'login.html')
        
def registerPage(request):
    if request.method=='POST':
        username = request.POST['uname']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password= request.POST['password']
        reg = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        reg.save()
        return redirect('/Login')
        #return HttpResponse('user register successful')
        
    return render(request,"register.html")


def logoutPage(request):
    logout(request)
    return render(request,'login.html')

def homePageData(request):
    products = Product.objects.all()
    data = {
        "products":products}
    if not data:
        return HttpResponse('error')
    return render(request,'index.html',data)

def addProduct(request):    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
        return HttpResponse('Error data not saved!')
    form = ProductForm()
    return render(request,'add_product_section.html',{'form':form})

def dog_info(request):
    return render(request,'dog_info.html')

def viewDetail(request,id):
    
    dogs = Product.objects.filter(p_category = 'DOG').order_by('-id')[:3]
    data = {'product':product}
    return render(request,'detail.html',data)

def viewMore(request,id):
    print(id)
    product=Product.objects.filter(id=id).all()
    data={'product':product}
    return render(request,'view_more.html',data)
