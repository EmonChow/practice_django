from rest_framework import serializers

from fee_generation.models import FeeGeneration


class FeeGenerationSerializer(serializers.ModelSerializer):
	class Meta:
		model = FeeGeneration
		fields = '__all__'
