from django.urls import path
from .views import list_orders_view, create_order_view, edit_order_view

urlpatterns = [
    path('', list_orders_view, name='list_orders'),
    path('create/', create_order_view, name='create_order'),
    path('edit/<int:pk>/', edit_order_view, name='edit_order'),
]
