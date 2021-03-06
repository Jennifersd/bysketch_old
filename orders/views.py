from django.shortcuts import render, redirect,  get_object_or_404
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
from .task import order_created
from django.contrib.auth.models import User



def order_create(request):
    cart = Cart(request)
    #user = User.objects.get(username=request.user)

    #username = None
    #if request.user.is_authenticated():
    #    username = request.user.username
    #user_order = username

   
    if request.method == 'POST':

        form = OrderCreateForm(request.POST,  instance=request.user)
        #form = OrderCreateForm(request.POST, instance=user_order)
        #form = OrderCreateForm(request.POST, instance=request.user.order)
        if form.is_valid():
            order.users.add(form.request.user)
            order = form.save(commit=False)
            order.user = request.user
            order.some_field = 'some_value'
            #order.user = User.objects.get(request.user.username) # and this to get the currently logged in user
            #order.user = User.objects.get(id=request.user.username)
            form.save_m2m()  # to commit the new info
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
        form = OrderCreateForm(instance=request.user)
        #form = OrderCreateForm(instance=user_order)
        #request.session.modified = True
       
    #try:
    #    order = request.user.order
    #except Order.DoesNotExist:
        #order = Order.objects.create(user=request.user)
        #user_order = Order.objects.get(user=request.user)
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


