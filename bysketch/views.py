from django.shortcuts import render
from shop import views
from shop.models import Product, Category

#View home Page
def home(request, category_slug=None):
    products = Product.objects.all() #Show all   y [:2] indica la cantidad de item a mostrar
    #series = TutorialSeries.objects.filter(archived=False).order_by('-id')[:3]
    
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    template = 'home.html'
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, template, context)