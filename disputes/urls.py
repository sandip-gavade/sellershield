from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_disputes, name='list_disputes'),
    path('create/', views.create_dispute, name='create_dispute'),
    path('<int:dispute_id>/edit/', views.edit_dispute, name='edit_dispute'),
]
