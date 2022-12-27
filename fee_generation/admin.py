from django.contrib import admin

from fee_generation.models import FeeGeneration


# Register your models here.

@admin.register(FeeGeneration)
class FeeGeneration(admin.ModelAdmin):
    list_display = [field.name for field in FeeGeneration._meta.fields]
