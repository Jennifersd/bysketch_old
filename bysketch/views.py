from django.shortcuts import render

from shop.models import Product

#View home Page
def home(request):
    products = Product.objects.all() #Show all   y [:2] indica la cantidad de item a mostrar
    #series = TutorialSeries.objects.filter(archived=False).order_by('-id')[:3]
    template = 'home.html'
    context = {'products': products}
    return render(request, template, context)