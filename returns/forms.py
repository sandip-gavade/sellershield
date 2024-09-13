from django import forms
from .models import Return


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['return_id', 'order', 'agent', 'return_reason', 'return_tracking_number',
                  'return_date', 'flagged_as_suspicious', 'validation_status']
