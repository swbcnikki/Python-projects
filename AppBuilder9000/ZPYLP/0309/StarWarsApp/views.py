from django.shortcuts import render, HttpResponse
from .form import ProductForm
from .models import Product


def home(request):
    return render(request, "StarWarsApp/SW_Home.html")


def SW_AddProduct(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
        form = ProductForm()
    context = {'form': form}
    return render(request, "StarWarsApp/SW_AddProduct.html", context)


def SW_store(request):
    products = Product.object.all()  # get products from db

    return render(request, "StarWarsApp/SW_store.html", {'products': products})


def SW_Details(request, pk):
    product = Product.object.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'StarWarsApp/SW_Details.html', context)
