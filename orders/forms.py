from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_id', 'item', 'customer_name',
                  'customer_email', 'order_total', 'status']
