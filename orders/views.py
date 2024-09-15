from django.template.loader import render_to_string
from django.http import JsonResponse
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .models import Order
from .forms import OrderForm


def list_orders_view(request):
    orders = Order.objects.all().order_by('-order_date')
    paginator = Paginator(orders, 10)  # 10 orders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Always render the order table along with the create button
    return render(request, 'orders/partials/order_table.html', {'page_obj': page_obj})


# def create_order_view(request):
#     if request.method == 'POST':
#         print('saving order form')
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Return a JSON response indicating success
#             return JsonResponse({"message": "Order created successfully"}, status=200)
#     else:
#         form = OrderForm()

#     return render(request, 'orders/partials/order_form.html', {'form': form})


# def edit_order_view(request, pk):
#     order = get_object_or_404(Order, pk=pk)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             # Return a JSON response indicating success
#             return JsonResponse({"message": "Order updated successfully"}, status=200)
#     else:
#         form = OrderForm(instance=order)

#     return render(request, 'orders/partials/order_form.html', {'form': form, 'order': order})


def create_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

            # Return a 200 OK response with HX-Trigger for toast and list update
            response = JsonResponse(
                {"message": "Order created successfully"}, status=200
            )
            response["HX-Trigger"] = json.dumps({
                "showToast": {"message": "wow Order created successfully", "tags": "success"},
                "refreshOrderList": True  # Custom event to refresh the order list
            })
            return response
        else:
            # If the form is invalid, re-render the modal form with errors
            html_form = render_to_string(
                'orders/partials/order_form.html', {'form': form})
            return JsonResponse({"html_form": html_form}, status=400)

    else:
        form = OrderForm()
        return render(request, 'orders/partials/order_form.html', {'form': form})


def edit_order_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # Return a 200 OK response with HX-Trigger for toast and list update
            response = JsonResponse(
                {"message": "Order updated successfully"}, status=200)
            response["HX-Trigger"] = json.dumps({
                "showToast": {"message": "Order updated successfully", "tags": "success"},
                "refreshOrderList": True  # Custom event to refresh the order list
            })
            return response
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/partials/order_form.html', {'form': form, 'order': order})
