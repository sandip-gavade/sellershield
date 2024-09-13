from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

# Login view using a function-based approach


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to dashboard after successful login
                return redirect('dashboard')
            else:
                return HttpResponse("Invalid login credentials")
        else:
            return HttpResponse("Invalid form submission")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# Logout view using a function-based approach
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


# A simple view to render the dashboard after login
@never_cache
@login_required
def dashboard_view(request):
    if not request.user.is_authenticated:
        # Ensure only authenticated users can access the dashboard
        return redirect('login')
    return render(request, 'accounts/dashboard.html')


@login_required
def order_view(request):
    return render(request, 'orders/order.html')


@login_required
def return_view(request):
    return render(request, 'returns/return.html')


@login_required
def dispute_view(request):
    return render(request, 'disputes/dispute.html')
