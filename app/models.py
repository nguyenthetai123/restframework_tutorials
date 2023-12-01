from django.db import models

# Create your models here.
class Persons(models.Model):
    name= models.CharField(max_length=255)
    age= models.IntegerField()

class Employee(models.Model):
    name= models.CharField(max_length=155)
    email= models.EmailField()
    password= models.CharField(max_length=30)
    phone= models.CharField(max_length=10)


class Post(models.Model):
    title= models.CharField(max_length=144)
    content= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title