from django.shortcuts import render, redirect
from .models import Notification, Report, Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm, LoginForm


@login_required
def dashboard(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'waste/dashboard.html', {'notifications': notifications})


@login_required
def report_issue(request):
    if request.method == "POST":
        description = request.POST['description']
        photo_url = request.POST.get('photo_url', '')
        Report.objects.create(user=request.user, description=description, photo_url=photo_url)
        return redirect('dashboard')
    return render(request, 'waste/report_issue.html')


def events(request):
    events = Event.objects.all()
    return render(request, 'waste/events.html', {'events': events})


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'waste/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'waste/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')
