from django import forms
from django.contrib.auth.models import User

from .models import Order


class OrderCreateForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    
    class Meta:
        model = Order
        fields = ['user', 'address', 'postal_code', 'city']


#'first_name', 'last_name', 'email'