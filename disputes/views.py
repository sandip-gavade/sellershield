from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import DisputeCase
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator
from django.http import HttpResponse

# List view with pagination


from django.shortcuts import render, get_object_or_404, redirect
from .models import DisputeCase
from .forms import DisputeForm
from django.core.paginator import Paginator
from django.http import HttpResponse

# List view with pagination


def list_disputes(request):
    disputes = DisputeCase.objects.all().order_by('-created_at')
    paginator = Paginator(disputes, 5)  # Show 10 disputes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('HX-Request'):
        return render(request, 'disputes/partials/dispute_table.html', {'page_obj': page_obj})

    return render(request, 'disputes/dispute_list.html', {'page_obj': page_obj})

# Edit an existing dispute


def edit_dispute(request, dispute_id):
    dispute = get_object_or_404(DisputeCase, pk=dispute_id)
    if request.method == 'POST':
        form = DisputeForm(request.POST, instance=dispute)
        if form.is_valid():
            form.save()
            return redirect('list_disputes')
    else:
        form = DisputeForm(instance=dispute)

    return render(request, 'disputes/dispute_form.html', {'form': form})


def create_dispute(request):
    if request.method == 'POST':
        form = disputeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_disputes')
    else:
        form = disputeForm()

    return render(request, 'disputes/dispute_form.html', {'form': form})

# Edit an existing dispute
