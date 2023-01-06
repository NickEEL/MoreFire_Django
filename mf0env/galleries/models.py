from django.db import models
from mfevents.models import Event
from django.urls import reverse

# Create your models here.
class Gallery(models.Model):
    name = models.CharField('Gallery name', max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ImageField('Photo', upload_to='photos/', null=True)
    info = models.TextField('Photo info.', null=True, blank=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def get_absolute_url(self):
        k = {'gallery': self.gallery, 'photo_id': self.id}
        return reverse('photo', kwargs=k)
