from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
from .task import order_created
from django.contrib.auth.models import User


def order_create(request):
    cart = Cart(request)
    #user = User.objects.get(username=request.user)
    user = request.user

    #user_order = Order.objects.get(user=request.user)  
    #try:
    #    user_order = Order.objects.get(user=request.user) 
    #except Order.DoesNotExist:
    #    user_order = User.objects.filter(username=username).first()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, instance=user)
        #form = OrderCreateForm(request.POST, instance=request.user.order)
        if form.is_valid():
            
            order = form.save(commit=False)
            order.user = request.user
            #order.user = User.objects.get(request.user.username) # and this to get the currently logged in user
            #order.user = User.objects.get(id=request.user.username)
            order.save()  # to commit the new info
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            order_created(order.id, request)
            request.session['order_id'] = order.id
            #order_id = order.id
            
            # redirect to the payment
            return redirect('payment:process')

    else:
        form = OrderCreateForm(instance=user)
        #request.session.modified = True
       
    
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form })


#  self.object.created_by = self.request.user
 #       self.object.save()