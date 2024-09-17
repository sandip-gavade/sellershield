from django.forms import TextInput, Textarea, Select, NumberInput, CheckboxInput
from django import forms
from .models import DisputeCase


class DisputeForm(forms.ModelForm):
    class Meta:
        model = DisputeCase
        fields = [
            'return_obj', 'agent', 'reason_for_dispute', 'status',
            'financial_impact', 'resolution_notes', 'notification_sent'
        ]

        # Adding widgets to customize the form fields
        widgets = {
            # Read-only
            'return_obj': Select(attrs={'class': 'form-control'}),
            'agent': Select(attrs={'class': 'form-control'}),
            # Text area for detailed input
            'reason_for_dispute': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # Dropdown for status selection
            'status': Select(attrs={'class': 'form-control'}),
            # Decimal input
            'financial_impact': NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            # Optional text area
            'resolution_notes': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # Checkbox for notifications
            'notification_sent': CheckboxInput(attrs={'class': 'form-check-input'}),
        }
