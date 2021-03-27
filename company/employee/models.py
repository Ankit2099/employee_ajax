from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20, null=True)
    roll_no = models.IntegerField(null=True)
    class_name = models.CharField(max_length=2, null=True)


    def __str__(self):
        return self.name

