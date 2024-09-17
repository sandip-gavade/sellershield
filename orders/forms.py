
from django import forms
from .models import Order
from django.forms import TextInput, EmailInput, NumberInput, Select, DateTimeInput


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'order_id', 'item', 'customer_name',
                  'customer_email', 'order_total', 'status']

        # Adding widgets to customize the form fields
        widgets = {
            'order_id': TextInput(attrs={'class': 'form-control'}),
            'item': TextInput(attrs={'class': 'form-control'}),
            'customer_name': TextInput(attrs={'class': 'form-control'}),
            'customer_email': EmailInput(attrs={'class': 'form-control'}),
            'order_total': NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            # Dropdown for status selection
            'status': Select(attrs={'class': 'form-control'}),
        }
