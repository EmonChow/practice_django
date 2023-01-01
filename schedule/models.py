from django.conf import settings
from django.db import models

# Create your models here.


class Schedule(models.Model):
    title = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="+")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return str(self.title)


class ScheduleDay(models.Model):
    day = models.CharField(max_length=25)
    start_time = models.TimeField()
    end_time = models.TimeField()
    time_slot = models.PositiveIntegerField()
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='schedule_day')

    def __str__(self):
        return str(self.day)
