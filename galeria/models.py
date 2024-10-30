from django.db import models

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

class Artist(models.Model):
     """ Artista """
     name = models.CharField(max_length=100)
     biography = models.TextField()
     photo = models.ImageField(upload_to='artists/')
     pub_date = models.DateField(auto_now_add=True)

     def _str_(self):
          return self.name
     
     def get_absolute_url(self):
          return reverse('artist-list')

class Artwork(models.Model):
     """ Obra de arte """
     artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='artworks')
     title = models.CharField(max_length=100)
     description = models.TextField()
     image = models.ImageField(upload_to='artworks/')
     pub_date = models.DateField(auto_now_add=True)
     price = models.DecimalField(max_digits=10, decimal_places=2)

     def _str_(self):
          return self.title

     def get_absolute_url(self):
          return reverse('artwork-list')

@receiver(post_delete, sender=Artist)
def artist_delete(sender, instance, **kwargs):
     """ Borra la foto del artista al eliminar """
     instance.photo.delete(False)

@receiver(post_delete, sender=Artwork)
def artwork_delete(sender, instance, **kwargs):
     """ Borra la imagen de la obra de arte al eliminar """
     instance.image.delete(False)
