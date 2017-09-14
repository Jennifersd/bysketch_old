from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Order


def order_created(order_id, request):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    user = request.user.is_authenticated()   
    order = Order.objects.get(id=order_id)
    subject = 'Order number {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.user,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'django-shop-tutorial@myshop.com',
                          [request.user.email])
    return mail_sent
