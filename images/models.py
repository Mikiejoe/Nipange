from django.db import models

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='img/')
    dateadded = models.DateField(auto_now=True, auto_now_add=False)