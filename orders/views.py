from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .task import order_created
from django.contrib.auth.models import User


def order_create(request):
    cart = Cart(request)
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid(self):
            self.order = form.save(commit=False)
            self.order.user = self.request.user  # and this to get the currently logged in user
            self.order.save()  # to commit the new info
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            order_created(order.id, request)
            request.session['order_id'] = order.id
            # redirect to the payment
            return redirect('payment:process')

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form })





#  self.object.created_by = self.request.user
 #       self.object.save()