from django.contrib import admin

from department.models import department


# Register your models here.
@admin.register(department)
class department(admin.ModelAdmin):
    list_display = [field.name for field in department._meta.fields]