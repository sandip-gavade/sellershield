from django import forms
from .models import Return
from django.forms.widgets import TextInput, DateInput, Select, CheckboxInput


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['return_id', 'order', 'agent', 'return_reason', 'return_tracking_number',
                  'return_date', 'flagged_as_suspicious', 'validation_status']

        # Customizing labels for form fields
        labels = {
            'return_id': 'Return Reference Number',
            'order': 'Associated Order',
            'agent': 'Customer Agent',
            'return_reason': 'Reason for Return',
            'return_tracking_number': 'Tracking Number',
            'return_date': 'Date of Return',
            'flagged_as_suspicious': 'Flag as Suspicious',
            'validation_status': 'Validation Status',
        }

        # Adding widgets to customize the form fields
        widgets = {
            'return_id': TextInput(attrs={'class': 'form-control'}),
            'order': Select(attrs={'class': 'form-control ', 'readonly': 'readonly' }),
            'agent': Select(attrs={'class': 'form-control'}),
            'return_reason': Select(attrs={'class': 'form-control'}),
            'return_tracking_number': TextInput(attrs={'class': 'form-control'}),
            # HTML5 date picker
            'return_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'flagged_as_suspicious': CheckboxInput(attrs={'class': 'form-check-input'}),
            'validation_status': Select(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        # Accept the default order as a parameter
        default_order = kwargs.pop('default_order', None)
        super(ReturnForm, self).__init__(*args, **kwargs)
        
        if default_order:
            # Set the initial value for the 'order' field to the default order
            self.fields['order'].initial = default_order