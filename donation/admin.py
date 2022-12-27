from django.contrib import admin

from donation.models import *



# Register your models here.

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in PaymentMethod._meta.fields]


@admin.register(PaymentMethodDetail)
class PaymentMethodDetailAdmin(admin.ModelAdmin):
	list_display = [field.name for field in PaymentMethodDetail._meta.fields]


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Donation._meta.fields]


@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Cause._meta.fields]


@admin.register(CauseContent)
class CauseContentAdmin(admin.ModelAdmin):
	list_display = [field.name for field in CauseContent._meta.fields]


@admin.register(CauseContentImage)
class CauseContentImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in CauseContentImage._meta.fields]


@admin.register(MonthlySubscription)
class MonthlySubscriptionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in MonthlySubscription._meta.fields]

