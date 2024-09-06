from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator  # it is used for paginator
# Create your views here.

# we can all know that django can follow a mvt architecture for first we can create a models.py
# and after that we can make a view in a view.py
# and after that we can make a template in a templates folder
# in it we have a one function which name is index and it have a one parivale product_obectis we can store in a display on it pages


def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:    # it is used for work of a search box
        product_objects = product_objects.filter(title__icontains=item_name)
    # paginator code
    # it used to combined a page in a 4
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        order = Order(items=name, name=name, email=email,
                      address=address, city=city, state=state, zipcode=zipcode)
        order.save()

    return render(request, 'shop/checkout.html')
