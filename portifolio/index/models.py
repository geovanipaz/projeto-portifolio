from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.forms import CharField

# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self) -> str:
        return self.title
    
class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)
    
    def __str__(self) -> str:
        return self.title
    
class client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)
    
    def __str__(self) -> str:
        return self.name