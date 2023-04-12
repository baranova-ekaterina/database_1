from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.object.all()

    if sort == 'name':
        result = phones.order_by('name')
    if sort == 'min_price':
        result = phones.order_by('price')
    if sort == 'max_price':
        result = phones.order_by('price').reverse()

    context = {'phones' : result}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone' : phone}
    return render(request, template, context)
