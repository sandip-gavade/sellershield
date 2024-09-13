from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_returns, name='list_returns'),
    path('create/', views.create_return, name='create_return'),
    path('<int:return_id>/edit/', views.edit_return, name='edit_return'),
]
