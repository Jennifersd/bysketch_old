from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    context = { 'category': category, 'categories': categories, 'products': products}
    template = 'shop/product/list.html'

    return render(request, template, context)


def product_detail(request, product_id, slug):
    product = get_object_or_404(Product,
                                id=product_id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    context =  {'product': product, 'cart_product_form': cart_product_form}
    template = 'shop/product/detail.html'
    return render(request, template, context)