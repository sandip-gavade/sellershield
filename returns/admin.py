from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Return

class ReturnAdmin(admin.ModelAdmin):
    list_display = ('return_id', 'order', 'agent', 'return_reason', 'validation_status', 'return_date')
    search_fields = ('return_id', 'order__order_id', 'return_reason')
    list_filter = ('validation_status', 'flagged_as_suspicious', 'return_date')
    ordering = ('-return_date',)

admin.site.register(Return, ReturnAdmin)
