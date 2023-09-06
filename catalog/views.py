from django.shortcuts import render

from catalog.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Skystore'
    }
    return render(request, 'catalog/index.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': product_item.title,
        'price': product_item.price,
        'body': product_item.body,
        'category': product_item.category,
        'creation_date': product_item.creation_date,
        'change_date': product_item.change_date,
        'preview': product_item.preview
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
