from django.urls import path
from . import views

app_name = 'waste'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report_issue, name='report_issue'),
    path('events/', views.events, name='events'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
