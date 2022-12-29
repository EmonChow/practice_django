from django.db import models

# Create your models here.


class department(models.Model):
    name = models.CharField(max_length=45)
    category = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    department_members = models.IntegerField()


