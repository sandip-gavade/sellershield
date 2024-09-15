import json
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from .models import Return
from .forms import ReturnForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


def list_returns_view(request):
    returns = Return.objects.all().order_by('-return_date')
    paginator = Paginator(returns, 5)  # 10 returns per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'returns/return_table.html', {'page_obj': page_obj})


def create_return_view(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.save()
            response = JsonResponse(
                {"message": "Return created successfully"}, status=200)
            response["HX-Trigger"] = json.dumps({
                "showToast": {"message": "Return created successfully", "tags": "success"},
                "refreshReturnList": True
            })
            return response
        else:
            html_form = render_to_string(
                'returns/return_form.html', {'form': form})
            return JsonResponse({"html_form": html_form}, status=400)
    else:
        form = ReturnForm()
        return render(request, 'returns/return_form.html', {'form': form})


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
