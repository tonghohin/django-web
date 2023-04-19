from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    return render(request, "products/product_detail.html", {"product": obj})


def dynamic_product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    return render(request, "products/product_detail.html", {"product": obj})


def product_create_view(request):
    initial_data = {"title": "Initial titie"}  # Set initial values of the form
    obj = Product.objects.get(
        id=1
    )  # Grab data from database to be initial values of the form

    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)

    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = ProductForm()

    return render(request, "products/product_create.html", {"form": form})


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../")
    return render(request, "products/product_delete.html", {"product": obj})


def product_list_view(request):
    queryset = Product.objects.all()
    return render(request, "products/product_list.html", {"product_list": queryset})
