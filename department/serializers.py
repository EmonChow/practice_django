from rest_framework import serializers

from department.models import department


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = "__all__"
