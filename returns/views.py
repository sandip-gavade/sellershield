from django.shortcuts import render, get_object_or_404, redirect
from .models import Return
from .forms import ReturnForm
from django.core.paginator import Paginator
from django.http import HttpResponse

# List view with pagination


def list_returns(request):
    returns = Return.objects.all().order_by('-return_date')
    paginator = Paginator(returns, 5)  # Show 10 returns per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('HX-Request'):
        return render(request, 'returns/partials/return_table.html', {'page_obj': page_obj})

    return render(request, 'returns/return_list.html', {'page_obj': page_obj})

# Create a new return


def create_return(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_returns')
    else:
        form = ReturnForm()

    return render(request, 'returns/return_form.html', {'form': form})

# Edit an existing return


def edit_return(request, return_id):
    return_instance = get_object_or_404(Return, pk=return_id)
    if request.method == 'POST':
        form = ReturnForm(request.POST, instance=return_instance)
        if form.is_valid():
            form.save()
            return redirect('list_returns')
    else:
        form = ReturnForm(instance=return_instance)

    return render(request, 'returns/return_form.html', {'form': form})
