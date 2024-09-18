from ast import Return
from django.db import models
from returns.models import Return
from django.contrib.auth.models import User
# Create your models here.

# Choices for Dispute Statuses
DISPUTE_STATUS_CHOICES = [
    ('Open', 'Open'),
    ('Resolved', 'Resolved'),
    ('Rejected', 'Rejected'),
]


class DisputeCase(models.Model):
    case_id = models.AutoField(primary_key=True)
    return_obj = models.ForeignKey(
        'returns.Return', related_name='disputes', on_delete=models.CASCADE)
    agent = models.ForeignKey(
        User, related_name='disputes', on_delete=models.CASCADE, default=1)
    reason_for_dispute = models.TextField()
    status = models.CharField(max_length=50, choices=[(
        'Open', 'Open'), ('Resolved', 'Resolved'), ('Rejected', 'Rejected')], default='Open')
    financial_impact = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolution_notes = models.TextField(blank=True, null=True)
    notification_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Dispute {self.case_id} for Return {self.return_obj.return_id}"
