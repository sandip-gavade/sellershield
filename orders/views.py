from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Order
from .forms import OrderForm


def list_orders_view(request):
    orders = Order.objects.all().order_by('-order_date')
    paginator = Paginator(orders, 5)  # 10 orders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Always render the order table along with the create button
    return render(request, 'orders/partials/order_table.html', {'page_obj': page_obj})


def create_order_view(request):
    if request.method == 'POST':
        print('saving order form')
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'orderListChanged'})
    else:
        print('empty order form')
        form = OrderForm()

    return render(request, 'orders/partials/order_form.html', {'form': form})


def edit_order_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'orderListChanged'})
    else:
        form = OrderForm(instance=order)

    return render(request, 'orders/partials/order_form.html', {'form': form, 'order': order})
