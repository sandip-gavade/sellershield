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

        # Customizing labels for form fields
        labels = {
            'return_obj': 'Associated Return',
            'agent': 'Assigned Agent',
            'reason_for_dispute': 'Dispute Reason',
            'status': 'Dispute Status',
            'financial_impact': 'Financial Impact',
            'resolution_notes': 'Resolution Notes',
            'notification_sent': 'Notification Sent to Seller',
        }

        # Adding widgets to customize the form fields
        widgets = {
            # Read-only
            'return_obj': Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'agent': Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
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
    def __init__(self, *args, **kwargs):
        # Accept default return_obj and agent as parameters
        default_return_obj = kwargs.pop('default_return_obj', None)
        default_agent = kwargs.pop('default_agent', None)
        super(DisputeForm, self).__init__(*args, **kwargs)

        # Set default values for return_obj and agent if provided
        if default_return_obj:
            self.fields['return_obj'].initial = default_return_obj
        if default_agent:
            self.fields['agent'].initial = default_agent