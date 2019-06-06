from django.shortcuts import render
from product.models import Category, Product


# Create your views here.
def index(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {'page': 'home', 'category': category, 'products': products}
    return render(request, 'index.html', context)
