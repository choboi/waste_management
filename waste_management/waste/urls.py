from django.urls import path
from . import views

app_name = 'waste'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('report/', views.report_issue, name='report_issue'),
    path('events/', views.events, name='events'),
]
