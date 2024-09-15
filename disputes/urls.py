from django.urls import path
from .views import list_disputes_view, create_dispute_view, edit_dispute_view

urlpatterns = [
    path('', list_disputes_view, name='list_disputes'),
    path('create/', create_dispute_view, name='create_dispute'),
    path('edit/<int:pk>/', edit_dispute_view, name='edit_dispute'),
]
