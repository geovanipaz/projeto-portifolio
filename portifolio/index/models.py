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