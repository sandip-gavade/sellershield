from .models import Return, DisputeCase
import json
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from .models import DisputeCase
from .forms import DisputeForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def list_disputes_view(request):
    disputes = DisputeCase.objects.all().order_by('-case_id')
    paginator = Paginator(disputes, 5)  # 10 disputes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'disputes/dispute_table.html', {'page_obj': page_obj})

@login_required
def create_dispute_view(request, return_id):
    return_obj = get_object_or_404(Return, return_id=return_id)
    default_agent = request.user # Use the logged-in user as the default agent

    if request.method == 'POST':
        form = DisputeForm(request.POST)
        if form.is_valid():
            dispute_instance = form.save(commit=False)
            dispute_instance.return_obj = return_obj  # Associate dispute with the return
            dispute_instance.save()

            # On success, trigger toast and redirect to disputes list
            response = JsonResponse(
                {"message": "Dispute created successfully"}, status=200)
            response["HX-Trigger"] = json.dumps({
                "showToast": {"message": "Dispute created successfully", "tags": "success"},
                "refreshDisputeList": True
            })
            return response
        else:
            # If the form is invalid, return the form with errors
            html_form = render_to_string(
                'disputes/dispute_form.html', {'form': form})
            return JsonResponse({"html_form": html_form}, status=400)

    else:
        # form = DisputeForm()
        form = DisputeForm(default_return_obj=return_obj, default_agent=default_agent)
        context = {'form': form, 'return': return_obj}
        return render(request, 'disputes/dispute_form.html', context)


@login_required
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
