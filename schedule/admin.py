from django.contrib import admin

from schedule.models import Schedule, ScheduleDay


@admin.register(Schedule)
class Schedule(admin.ModelAdmin):
    list_display = [field.name for field in Schedule._meta.fields]


@admin.register(ScheduleDay)
class ScheduleDay(admin.ModelAdmin):
    list_display = [field.name for field in ScheduleDay._meta.fields]