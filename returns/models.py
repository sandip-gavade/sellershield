from django.db import models
from orders.models import Order
from django.contrib.auth.models import User

# Choices for Return Statuses
RETURN_STATUS_CHOICES = [
    ('Valid', 'Valid'),
    ('Suspicious', 'Suspicious'),
    ('Invalid', 'Invalid'),
]

# Choices for Return Reasons
RETURN_REASON_CHOICES = [
    ('damaged', 'Damaged Product'),
    ('wrong_item', 'Wrong Item Shipped'),
    ('not_needed', 'No Longer Needed'),
    ('size_issue', 'Size Issue'),
    ('other', 'Other'),
]


class Return(models.Model):
    return_id = models.CharField(max_length=255, unique=True)
    order = models.ForeignKey(
        Order, related_name='returns', on_delete=models.CASCADE)
    agent = models.ForeignKey(
        User, related_name='returns', on_delete=models.CASCADE, default=1)
    # Use choices for return reason
    return_reason = models.CharField(
        max_length=255, choices=RETURN_REASON_CHOICES, default='other')
    return_tracking_number = models.CharField(
        max_length=255, blank=True, null=True)
    return_date = models.DateTimeField()
    flagged_as_suspicious = models.BooleanField(default=False)
    validation_status = models.CharField(
        max_length=255, choices=RETURN_STATUS_CHOICES, default='Valid')

    def __str__(self):
        return f"Return {self.return_id} for Order {self.order.order_id}"

    def can_view(self, user):
        """Check if a user can view this return"""
        return self.order.seller == user or user == self.agent or user.is_superuser
