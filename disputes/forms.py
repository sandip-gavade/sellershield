from django import forms
from .models import DisputeCase


class DisputeForm(forms.ModelForm):
    class Meta:
        model = DisputeCase
        fields = ['return_obj', 'reason_for_dispute', 'status',
                  'financial_impact', 'resolution_notes', 'notification_sent']
