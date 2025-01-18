from django.contrib import admin
from .models import Notification, Report, Event


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'date')
    search_fields = ('user__username', 'message')
    list_filter = ('date',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'status', 'date')
    search_fields = ('user__username', 'description', 'status')
    list_filter = ('status', 'date')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date')
    search_fields = ('title', 'location')
    list_filter = ('date',)