from django.db import models

# Create your models here.
class Teach(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    age= models.IntegerField()

    def __str__(self):
        return self.name