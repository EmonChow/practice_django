from rest_framework import serializers

from schedule.models import Schedule, ScheduleDay


class ScheduleDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDay
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    schedule_day = ScheduleDaysSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"
