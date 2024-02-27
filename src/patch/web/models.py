from django.db import models

# Create your models here.

class Service (models.Model):
    title = models.CharField(max_length=255)
    discription=models.TextField()

class Brand (models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='brands')

class Contact (models.Model):
    image = models.FileField(upload_to='contacts')

class Friend (models.Model):
    title = models.CharField(max_length=255)
    discription=models.TextField() 

class FaqCategory (models.Model):
    title = models.CharField(max_length=255)
