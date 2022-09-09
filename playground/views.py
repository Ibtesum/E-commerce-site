from django.shortcuts import render
from store.models import Product
# Create your views here.

def say_hello(request):    
    queryset = Product.objects.filter(title__icontains='coffee')

    return render(
        request, 'hello.html', {'name': 'Aninda', 'products': list(queryset)})
    