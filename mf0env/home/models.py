from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save

from mfevents.models import Event
from music.models import Track, Mix

# Create your models here.
class Photohome(models.Model):
    hm_image = models.ImageField('Home page image', upload_to='home_images/', null=True, blank=True)


class Infohome(models.Model):
    info = models.TextField('Home information')


class Links(models.Model):
    LINK_TYPE_CHOICES = [
        ('band', 'Bandcamp'),
        ('mixc', 'MixCloud'),
        ('fb', 'Facebook'),
        ('twit', 'Twitter'),
        ('inst', 'Instagram'),
        ('other', 'Other'),
    ]

    name = models.CharField('Link name', max_length=100, default='name')
    type_lnk = models.CharField('Type', max_length=20, choices=LINK_TYPE_CHOICES, default='Other')
    mflink = models.BooleanField('More Fire link', default=False)
    link_url = models.URLField('Link url')
    logo_lnk = models.ImageField('Link Logo', upload_to= 'logo_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class CalendarEntry(models.Model):
    event_bol = models.BooleanField('Event True/False', default=False)
    mix_bol = models.BooleanField('Mix True/False', default=False)
    track_bol = models.BooleanField('Track True/False', default=False)
    date = models.DateField('Entrydate', null=True, blank=True)
    event = models.OneToOneField(Event, on_delete=models.CASCADE, null=True, blank=True)
    mix = models.OneToOneField(Mix, on_delete=models.CASCADE, null=True, blank=True)
    track = models.OneToOneField(Track, on_delete=models.CASCADE, null=True, blank=True)
    created_dt = models.DateTimeField('Date created', auto_now_add=True)
    edited_dt = models.DateTimeField('Date edited', auto_now=True)

    def __str__(self):
        if self.event_bol:
            event = "Event"
            return event
        elif self.mix_bol:
            mix = "Mix"
            return mix
        elif self.track_bol:
            track = "Track"
            return track
        else:
            print("Error: Checkeck Booleans")


    @property
    def start_date(self):
        e = self.event_bol
        m = self.mix_bol
        t = self.track_bol
        st_date = ''
        if e:
            st_date = self.event.start_dt
        elif m:
            st_date = self.mix.release_date
        elif t:
            st_date = self.track.release_date
        else:
            Print("Error: Check dates or booleans!")
        return st_date

    @property
    def finish_date(self):
        e = self.event_bol
        m = self.mix_bol
        t = self.track_bol
        fn_date = ''
        if e:
            fn_date = self.event.finish_dt
        elif m:
            fn_date = self.mix.release_date
        elif t:
            fn_date = self.track.release_date
        else:
            Print("Error: Check dates or booleans!")
        return fn_date


    def get_absolute_url(self):
        n = '' # sets the name url variable name
        k = {} # sets the kwargs variable
        if self.event_bol == True:
            n = 'event-profile'
            k = {'event_id': self.event.id}
        elif self.mix_bol == True:
            n = 'mix-profile'
            k = {'mix_id': self.mix.id}
        elif self.track_bol == True:
            n = 'track_profile'
            k = {'track_id': self.track.id}
        else:
            Print("Error: Booleans boxes not correct, check if 0 or >1 boxes checked!")

        return reverse(n, kwargs=k)


def create_entry(sender, **kwargs):
    if kwargs['created']:
        if sender == Event:
            entry = CalendarEntry.objects.create(
                event_bol=True,
                date=kwargs['instance'].start_dt,
                event=kwargs['instance'],
            )
        elif sender == Mix:
            entry = CalendarEntry.objects.create(
                mix_bol=True,
                date=kwargs['instance'].release_date,
                mix=kwargs['instance'],
            )
        elif sender == Track:
            entry = CalendarEntry.objects.create(
                track_bol=True,
                date=kwargs['instance'].release_date,
                track=kwargs['instance'],
            )
        else:
            print("Error: somethings up!")


post_save.connect(create_entry, sender= Event)
post_save.connect(create_entry, sender= Mix)
post_save.connect(create_entry, sender= Track)