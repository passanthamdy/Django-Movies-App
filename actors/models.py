from email.mime import image
from django.db import models
from django.forms import ImageField

# Create your models here.

GENDER=(
    ('FEMALE','Female'),
    ('MALE','Male'),
    ('OTHER','other')
)
class Actor(models.Model):
    name=models.CharField( max_length=50)
    gender=models.CharField(choices=GENDER, max_length=50)
    age=models.IntegerField(default=15)
    profile_picture = models.ImageField(upload_to='actors/') 

    def __str__(self):
        return self.name
    