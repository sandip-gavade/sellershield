from django.urls import path
from .views import list_returns_view, create_return_view, edit_return_view

urlpatterns = [
    path('', list_returns_view, name='list_returns'),
    path('create/', create_return_view, name='create_return'),
    path('edit/<int:pk>/', edit_return_view, name='edit_return'),
]
