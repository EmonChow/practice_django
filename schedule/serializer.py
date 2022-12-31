
from rest_framework import serializers

from schedule.models import Schedule, ScheduleDay


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDay
        fields = "__all__"
