from django.contrib import admin
from .models import DisputeCase


class DisputeCaseAdmin(admin.ModelAdmin):
    list_display = ('case_id', 'return_obj', 'agent', 'status',
                    'financial_impact', 'created_at', 'updated_at')
    search_fields = ('case_id', 'return_obj__return_id', 'reason_for_dispute')
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('-created_at',)


admin.site.register(DisputeCase, DisputeCaseAdmin)
