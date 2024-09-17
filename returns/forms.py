from django import forms
from .models import Return
from django.forms.widgets import TextInput, DateInput, Select, CheckboxInput


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['return_id', 'order', 'agent', 'return_reason', 'return_tracking_number',
                  'return_date', 'flagged_as_suspicious', 'validation_status']

        # Adding widgets to customize the form fields
        widgets = {
            'return_id': TextInput(attrs={'class': 'form-control'}),
            'order': Select(attrs={'class': 'form-control'}),
            'agent': Select(attrs={'class': 'form-control'}),
            'return_reason': Select(attrs={'class': 'form-control'}),
            'return_tracking_number': TextInput(attrs={'class': 'form-control'}),
            # HTML5 date picker
            'return_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'flagged_as_suspicious': CheckboxInput(attrs={'class': 'form-check-input'}),
            'validation_status': Select(attrs={'class': 'form-control'}),
        }
