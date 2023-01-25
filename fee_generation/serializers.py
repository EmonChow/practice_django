from rest_framework import serializers

from authentication.serializers import AdminUserMinimalListSerializer
from fee_generation.models import FeeGeneration


class FeeGenlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeeGeneration
        fields = '__all__'


class FeeGenerationMinimalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeeGeneration
        fields = ['id', 'member']


class FeeGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeGeneration
        fields = '__all__'
