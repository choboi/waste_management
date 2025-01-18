from django.shortcuts import render, redirect
from .models import Notification, Report, Event
from django.contrib.auth.decorators import login_required


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
