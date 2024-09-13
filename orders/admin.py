from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'seller', 'customer_name', 'status', 'order_date', 'order_total')
    search_fields = ('order_id', 'customer_name', 'customer_email')
    list_filter = ('status', 'order_date', 'seller')
    ordering = ('-order_date',)

admin.site.register(Order, OrderAdmin)
