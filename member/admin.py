import imp
from django.contrib import admin

from member.models import *




# Register your models here.


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Member._meta.fields]


@admin.register(ExecutiveMember)
class ExecutiveMemberAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ExecutiveMember._meta.fields]


@admin.register(AdviserMember)
class AdviserMemberAdmin(admin.ModelAdmin):
	list_display = [field.name for field in AdviserMember._meta.fields]


@admin.register(GeneralMember)
class GeneralMemberAdmin(admin.ModelAdmin):
	list_display = [field.name for field in GeneralMember._meta.fields]


