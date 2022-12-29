from django.db import models

from member.models import Member


# Create your models here.


class FeeGeneration(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='fee_generation')
    date = models.DateTimeField()
    amount = models.IntegerField()
    note = models.TextField(null=True, blank=True)
