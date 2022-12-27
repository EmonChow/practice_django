from django.conf import settings 
from django.db import models

from authentication.models import User

# Create your models here.


class Member(User):
    father_name = models.CharField(max_length=255, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    spouse_name = models.CharField(max_length=255, null=True, blank=True)
    village = models.CharField(max_length=255, null=True, blank=True)
    post_office = models.CharField(max_length=255, null=True, blank=True)
    union = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=255, null=True, blank=True)


class ExecutiveMember(models.Model):
    member = models.OneToOneField(Member, on_delete=models.PROTECT, related_name='executive_member')
    designation = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)


class AdviserMember(models.Model):
    member = models.OneToOneField(Member, on_delete=models.PROTECT, related_name='adviser_member')
    designation = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)


class GeneralMember(models.Model):
    member = models.OneToOneField(Member, on_delete=models.PROTECT, related_name='general_member')
    designation = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)


