from django.db import models

# Create your models here.

class Student(models.Model):

    name=models.CharField(max_length=200)

    course=models.CharField(max_length=200)

    fees=models.PositiveIntegerField()

    def __str__(self):
        return self.name
