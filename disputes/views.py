import json
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from .models import DisputeCase
from .forms import DisputeForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


def list_disputes_view(request):
    disputes = DisputeCase.objects.all().order_by('-case_id')
    paginator = Paginator(disputes, 10)  # 10 disputes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'disputes/dispute_table.html', {'page_obj': page_obj})


def create_dispute_view(request):
    if request.method == 'POST':
        form = DisputeForm(request.POST)
        if form.is_valid():
            form.save()
            response = JsonResponse(
                {"message": "Dispute created successfully"}, status=200)
            response["HX-Trigger"] = json.dumps({
                "showToast": {"message": "Dispute created successfully", "tags": "success"},
                "refreshDisputeList": True
            })
            return response
        else:
            html_form = render_to_string(
                'disputes/dispute_form.html', {'form': form})
            return JsonResponse({"html_form": html_form}, status=400)
    else:
        form = DisputeForm()
        return render(request, 'disputes/dispute_form.html', {'form': form})


def edit_dispute_view(request, pk):
    dispute = get_object_or_404(DisputeCase, pk=pk)
    if request.method == 'POST':
        form = DisputeForm(request.POST, instance=dispute)
        if form.is_valid():
            form.save()
            response = JsonResponse(
                {"message": "Dispute updated successfully"}, status=200)
            response["HX-Trigger"] = json.dumps({
                "showToast": {"message": "Dispute updated successfully", "tags": "success"},
                "refreshDisputeList": True
            })
            return response
    else:
        form = DisputeForm(instance=dispute)
        return render(request, 'disputes/dispute_form.html', {'form': form, 'dispute': dispute})
