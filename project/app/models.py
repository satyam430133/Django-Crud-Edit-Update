from django.db import models

# Create your models here.

class Stu(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    class Meta():
        pass