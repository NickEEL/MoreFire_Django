from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import date
from music.models import Artist, Genre, Soundsystem, Track, Mix


# Create your models here.
class EventCrew(models.Model):
    name = models.CharField('Event Crew', max_length=120, default='')
    contact_name = models.CharField('Contact name', max_length=50, blank=True, null=True)
    contact_phone = models.CharField('Contact phone number', max_length=15, blank=True, null=True)
    contact_email = models.EmailField('Contact email', blank=True, null=True)
    website = models.URLField('website', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name



class Venue(models.Model):
    name = models.CharField('Venue name', max_length=120)
    location = models.CharField('Venue location', max_length=250, blank=True, null=True)
    postcode = models.CharField('Venue postcode', max_length=10, blank=True, null=True)
    website = models.URLField('Venue website', blank=True, null=True)
    contact_name = models.CharField('Venue contact', max_length=50, blank=True, null=True)
    contact_phone = models.CharField('Contact phone number',max_length=15, blank=True, null=True)
    contact_email = models.EmailField('Contact email', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)


    def __str__(self):
        return self.name


class Event(models.Model):
    #choices for event type
    EVENT_TYPE_CHOICES = [
        ('Sound System',(
            ('carnival_S', 'Carnival/Street Party'),
            ('club_S', 'Club '),
            ('club_S_sc', 'Club: Sound-Clash'),
            ('festival_S', 'Festival'),
                        )
        ),
        ('DJ',  (
            ('radio', 'Radio show'),
            ('carnival_dj', 'Carnival/Street Party (DJ)'),
            ('club_dj', 'Club (DJ)'),
            ('club_dj_sc', 'Club (DJ): Sound-Clash'),
            ('festival_dj', 'Festival (DJ)'),
            ('pub_dj', 'Pub (DJ)'),
                )
        ),
        ('private','Private Event'),
        ('workshop', 'Workshop'),

    ]
    EVENT_STATUS_CHOICES = [
            ('Plan', 'Planning'),
            ('Scheduled','Scheduled'),
            ('Cancelled','Cancelled'),
        ]

    name = models.CharField('Event name', max_length=150)
    organiser = models.ForeignKey(EventCrew, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    type = models.CharField('Type', max_length=20, choices=EVENT_TYPE_CHOICES, default='club_S')
    status = models.CharField('Status', max_length=20, choices=EVENT_STATUS_CHOICES, default='Plan')
    start_dt = models.DateTimeField('Event (start) time & date', default=timezone.now)
    finish_dt = models.DateTimeField('Event (finish) time & date',  default=timezone.now)
    finished = models.BooleanField('Event Finished', default=False)
    genre = models.ManyToManyField(Genre, related_name='event_genre')
    soundclash = models.BooleanField('Sounclash', default=False)
    soundsystem = models.ManyToManyField(Soundsystem, related_name='soundsystem')
    selectas = models.ManyToManyField(Artist, related_name='event_selectas', limit_choices_to={'artist_type__selecta':True})
    vocals = models.ManyToManyField(Artist, related_name='event_vocals', limit_choices_to={'artist_type__vocalist':True})
    instrumentals = models.ManyToManyField(Artist, related_name='event_instrumentals', limit_choices_to={'artist_type__instrumentalist':True})
    event_info = models.TextField('Information', null=True, blank=True)
    event_image = models.ImageField('Event Image', upload_to= 'event_images/', null=True, blank=True)
    event_url = models.URLField('Event website', blank=True, null=True)
    ticket_url = models.URLField('Ticket website', blank=True, null=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name

    @property
    def days_until(self):
        now = timezone.now()
        current_date = now.date()
        time_til = self.start_dt - now
        days_til = self.start_dt.date() - current_date
        days_til_strip = str(days_til).split(",", 1)[0]
        return days_til_strip

    def get_absolute_url(self):
        return reverse('event-profile', kwargs={'event_id': self.pk})



class EventEnquiry(models.Model):
    name = models.CharField('Name',max_length=50)
    email = models.EmailField('Email', blank=True, null=True)
    message = models.CharField('Message', max_length=300)
    created_dt =models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        return self.name
