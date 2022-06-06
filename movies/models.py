
from django.db import models
from actors.models import Actor
# Create your models here.
class Movie(models.Model):
    name=models.CharField( max_length=50)
    production_year=models.PositiveSmallIntegerField(blank=True, null=True)
    image= models.ImageField(upload_to='movies/', default='img.png') 
    actors=models.ManyToManyField("actors.Actor",)
    created_at=models.DateField(  auto_now_add=True)
    updated_at=models.DateField( auto_now=True)

    def __str__(self):
        return self.name
    
