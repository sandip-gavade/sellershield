import json
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from .models import Return
from .forms import ReturnForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Order, Return
from .forms import ReturnForm
import json
from django.contrib.auth.decorators import login_required

@login_required
def list_returns_view(request):
    returns = Return.objects.all().order_by('-return_date')
    paginator = Paginator(returns, 5)  # 10 returns per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'returns/return_table.html', {'page_obj': page_obj})


# def create_return_view(request):
#     if request.method == 'POST':
#         form = ReturnForm(request.POST)
#         if form.is_valid():
#             form.save()
#             response = JsonResponse(
#                 {"message": "Return created successfully"}, status=200)
#             response["HX-Trigger"] = json.dumps({
#                 "showToast": {"message": "Return created successfully", "tags": "success"},
#                 "refreshReturnList": True
#             })
#             return response
#         else:
#             html_form = render_to_string(
#                 'returns/return_form.html', {'form': form})
#             return JsonResponse({"html_form": html_form}, status=400)
#     else:
#         form = ReturnForm()
#         return render(request, 'returns/return_form.html', {'form': form})

@login_required
def create_return_view(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            return_instance = form.save(commit=False)
            return_instance.order = order  # Associate the return with the order
            return_instance.save()

            # On success, trigger toast and redirect to returns list
            response = JsonResponse(
                {"message": "Return created successfully"}, status=200)
            response["HX-Trigger"] = json.dumps({
                "showToast": {"message": "Return created successfully", "tags": "success"},
                "refreshReturnList": True
            })
            return response
        else:
            # If the form is invalid, return the form with errors
            html_form = render_to_string(
                'returns/return_form.html', {'form': form})
            return JsonResponse({"html_form": html_form}, status=400)

    else:
        # form = ReturnForm()
        form = ReturnForm(default_order=order)
        context = {'form': form, 'order': order }
        return render(request, 'returns/return_form.html', context)

@login_required
def edit_return_view(request, pk):
    return_instance = get_object_or_404(Return, pk=pk)
    if request.method == 'POST':
        form = ReturnForm(request.POST, instance=return_instance)
        if form.is_valid():
            form.save()
            response = JsonResponse(
                {"message": "Return updated successfully"}, status=200)
            response["HX-Trigger"] = json.dumps({
                "showToast": {"message": "Return updated successfully", "tags": "success"},
                "refreshReturnList": True
            })
            return response
    else:
        form = ReturnForm(instance=return_instance)
        return render(request, 'returns/return_form.html', {'form': form, 'return': return_instance})
