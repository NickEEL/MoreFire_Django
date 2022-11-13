from django.db import models
from django.utils import timezone



# Create your models here.
class Genre(models.Model):
    name = models.CharField('Musical Genre Name', max_length=100, default='')

    def __str__(self):
        return self.name



class Soundsystem(models.Model):
    name = models.CharField('Sound Name', max_length=100, default='')
    genre = models.ManyToManyField(Genre, related_name='sound_genre')
    rank = models.IntegerField('Sound rank', )
    location = models.CharField('Location', max_length=250, blank=True, null=True)
    contact_name = models.CharField('Contact', max_length=50, blank=True, null=True)
    contact_phone = models.CharField('Contact phone number', max_length=15, blank=True, null=True)
    contact_email = models.EmailField('Email', blank=True, null=True)
    sound_url = models.URLField('weblink', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField('Sound Name', max_length=100, default='')
    genre = models.ManyToManyField(Genre, related_name='group_genre')
    location = models.CharField('Location', max_length=250, blank=True, null=True)
    contact_name = models.CharField('Contact', max_length=50, blank=True, null=True)
    contact_phone = models.CharField('Contact phone number', max_length=15, blank=True, null=True)
    contact_email = models.EmailField('Email', blank=True, null=True)
    sound_url = models.URLField('weblink', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name



class Label(models.Model):
    name = models.CharField('Label Name', max_length=100, default='')
    location = models.CharField('Label location', max_length=250, blank=True, null=True)
    contact_name = models.CharField('Label contact', max_length=50, blank=True, null=True)
    contact_phone = models.CharField('Label phone number', max_length=15, blank=True, null=True)
    contact_email = models.EmailField('Label email', blank=True, null=True)
    website = models.URLField('Label web address', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name



class Studio(models.Model):
    name = models.CharField('Studio Name', max_length=100, default='')
    location = models.CharField('Studio location', max_length=250, blank=True, null=True)
    contact_name = models.CharField('Studiol contact', max_length=50, blank=True, null=True)
    contact_phone = models.CharField('Studio phone number', max_length=15, blank=True, null=True)
    contact_email = models.EmailField('Studio email', blank=True, null=True)
    website = models.URLField('Studio web address', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name



class ArtistType(models.Model):
    name = models.CharField('Artist Type Name', max_length=100, default='')
    selecta = models.BooleanField('Selecta (DJ, CDJ etc.) = true', default=False)
    vocalist = models.BooleanField('Vocalist (MC; Singer; Beatbox etc.) = true', default=False)
    instrumentalist = models.BooleanField('Instrumentist (including electronic) = True', default=False)

    def __str__(self):
        return self.name



class Artist(models.Model):
    name = models.CharField('Artist Name', max_length=100, default='')
    artist_type = models.ManyToManyField(ArtistType, related_name='artist_type')
    genre = models.ManyToManyField(Genre, related_name='artist_genre')
    rank = models.IntegerField('rank: Headline is low number',)
    crew = models.ForeignKey(Soundsystem, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField('Artist Location', max_length=100, null=True, blank=True)
    email = models.EmailField('Artist Email', null=True, blank=True)
    artist_url = models.URLField('Artist Website', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    class Meta:
        ordering = ['rank']

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField('Producer Name', max_length=100, default='')
    label = models.ManyToManyField(Label, related_name= 'Producer_labels')
    producer_location = models.CharField('Producer Location', max_length=100, null=True, blank=True)
    Producer_email = models.EmailField('Producer Email', null=True, blank=True)
    Producer_url = models.URLField('Producer Website', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name



class Track(models.Model):
    name = models.CharField('Track Name', max_length=200, default='')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    featured_artists = models.ManyToManyField(Artist, related_name='track_artists')
    genre = models.ManyToManyField(Genre,  related_name='track_genre')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, blank=True, null=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, blank=True, null=True)
    recorded_date = models.DateField('Track Recorded Date', default=timezone.now, null=True, blank=True)
    release_date = models.DateField('Track Release Date',default=timezone.now)
    track_url = models.URLField('Track webaddress', blank=True, null=True)
    track_embed = models.CharField('Embed Track html', max_length=500,blank=True, null=True )
    track_info =  models.TextField('Information', null=True, blank=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name



class Mix(models.Model):
    name = models.CharField('Mix Name', max_length=200, default='')
    dj = models.ForeignKey(Artist, on_delete=models.CASCADE , related_name='mix_dj')
    featured_artists = models.ManyToManyField(Artist, related_name='featured_artists', blank=True)
    genre = models.ManyToManyField(Genre,  related_name='mix_genre')
    recorded_date = models.DateField('Mix Recorded Date', default=timezone.now,  null=True, blank=True)
    release_date = models.DateField('Mix Release Date',default=timezone.now)
    mix_url = models.URLField('Mix weblink', blank=True, null=True)
    mix_embed = models.CharField('Embed mix html', max_length=500, blank=True, null=True)
    mix_info = models.TextField('Information', null=True, blank=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name
