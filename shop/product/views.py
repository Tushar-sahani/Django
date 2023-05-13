from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import Feedbackform
# Create your views here.

def index(request):
    product_numb = 4
    
    name = "the list more then"
    products = Product.objects.all()
    return render(request, "product/home.html",{
        "product_numd":product_numb,
        "name": name,
        "products":products,
        
        })

def signup(request):
    
    return render(request, "product/signup.html")

def suit(request,product):
    if product == "shirt" or product == "shocks" or product == "clothes" or product == "jense":
        return HttpResponse(f"This is list of suit {product}")
    else:
        return HttpResponse("Page not found")

def product_page(request,product_brand,product_slug):
    form  = Feedbackform(request.POST)
    product = Product.objects.get(slug = product_slug)
    if request.method =="GET":
        return render(request, "product/products.html",{
        "product": product,
        "forms":form,
        })
    else:
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, "product/products.html",{
        "product": product,
        "forms":form,
    })

    