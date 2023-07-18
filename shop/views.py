from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Category, Product, Cart, CartItem


def store(request, pk=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    if pk:
        category = get_object_or_404(Category, id=pk)
        products = Product.objects.filter(category=category)
    context = {
        'products': products,
        "item_count": products.count(),
        'categories': categories
    }

    return render(request, 'store.html', context=context)


def search(request):
    ctx = {}
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            products = Product.objects.filter(Q(title__icontains=keyword))
            product_count = products.count()
            ctx = {
                "products": products,
                "item_count": product_count
            }

    return render(request, 'search.html', ctx)

@login_required(login_url= 'login')
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, complete=False)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    return redirect('store')

@login_required(login_url= 'login')
def add_quantity(request, product_id):

    item, created = CartItem.objects.get_or_create(id=product_id)

    item.quantity += 1
    item.save()
    return redirect('test')

@login_required(login_url= 'login')
def sub_quantity(request, product_id):


    item, created = CartItem.objects.get_or_create(id=product_id)

    item.quantity -= 1
    item.save()
    if item.quantity < 1:
        item.delete()


    return redirect('test')


@login_required(login_url= 'login')
def test(request):
    try:
        cart = Cart.objects.get(user=request.user)
        items = CartItem.objects.filter(cart=cart)
        context = {
            'items' : items,
            'cart': cart,
            'count': items.count()
        }
        return render(request, 'cart.html', context=context)
    except Cart.DoesNotExist:
        return HttpResponse('not found')



@login_required(login_url= 'login')
def check_out(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    items = CartItem.objects.filter(cart=cart)
    for i in items:
        product = Product.objects.get(id=i.product.id)
        product.num_of_buy += i.quantity
        product.save()
    cart.complete = True

    return HttpResponse("پرداخت کامل شد.")




