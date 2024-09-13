from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Choices for Order Statuses
ORDER_STATUS_CHOICES = [
    ('Created', 'Created'),
    ('Payment Processing', 'Payment Processing'),
    ('Payment Failed', 'Payment Failed'),
    ('Payment Successful', 'Payment Successful'),
    ('Confirmed', 'Confirmed'),
    ('Inventory Check', 'Inventory Check'),
    ('Packing', 'Packing'),
    ('Shipped', 'Shipped'),
    ('Out for Delivery', 'Out for Delivery'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),
    ('Returned', 'Returned'),
    ('Refund Initiated', 'Refund Initiated'),
    ('Refund Completed', 'Refund Completed'),
]


class Order(models.Model):
    # Linking the order to the seller (User)
    seller = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE, default=1)
    order_id = models.CharField(max_length=255, unique=True)
    item = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default='Created')  # Status tracking
    # To log changes made to the order
    audit_trail = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.order_id} - {self.seller.username}"

    def can_view(self, user):
        """Check if a user can view this order"""
        return self.seller == user or user.is_superuser  # Seller or admin can view
