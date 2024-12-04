from django.db import models

# Create your models here.
class Teachers(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=False)
    email = models.CharField(max_length=150)
    joining_date = models.DateField()
    educational_background = models.JSONField(blank=True)
    salary = models.FloatField(null=False,blank=False)
