from django.test import TestCase
from home.models import *
from mfevents.models import *
from music.models import *
from galleries.models import *
from datetime import datetime, date, timedelta

""" Setup for all tests. Including model objects"""

def setUpModel(self):
    # home models objects
    self.photohome_test1 = Photohome.objects.create(
        hm_image = 'photohome_test1.jpg',
    )
    photohome_test1 = self.photohome_test1

    self.infohome_test1 = Infohome.objects.create(
        info = 'info test 1',
    )


    self.link_test1 = Links.objects.create(
        name = 'link test1',
        link_url = 'www.linktest1.net',
        logo_lnk = 'loglinktest1.png',
    )

    photohome_test1 = self.photohome_test1
    infohome_test1 = self.infohome_test1
    link_test1 = self.link_test1

    # mfevent models objects
    self.venue_test1 = Venue.objects.create(
        name = 'test venue1',
    )
    venue_test1 = self.venue_test1

    self.eventcrew_test1 = EventCrew.objects.create(
        name = 'testcrew1',
    )
    eventcrew_test1 = self.eventcrew_test1

    self.event_test1_scheduled = Event.objects.create(
        name = 'event test1',
        organiser = self.eventcrew_test1,
        venue = self.venue_test1,
        status = 'Scheduled',
        start_dt = datetime.utcnow() + timedelta(days=10),
        finish_dt = start_dt + timedelta(hours=10),
        finished = False,
        genre = self.genre_test1,
    )
    event_test1_scheduled = self.event_test1_scheduled

    self.event_test2_finished = Event.objects.create(
        name = 'event test2',
        organiser = self.eventcrew_test1,
        venue = self.venue_test1,
        status = 'Scheduled',
        start_dt = datetime.utcnow() - timedelta(days=10),
        finish_dt = start_dt + timedelta(hours=10),
        finished = True,
    )
    event_test2_finished = self.event_test2_finished


    # Music models
    self.genre_test1 = Genre.objects.create(
        name = 'genre test1',
    )
    genre_test1 = self.genre_test1

    self.artist_type_selecta_test1 = ArtistType.objects.create(
        name = 'artist type selecta test1',
        selecta = True,
    )
    artist_type_selecta_test1 = self.artist_type_selecta_test1

    self.artist_dj_test1 = Artist.objects.create(
        name = 'artist dj test1',
        artist_type = self.artist_type_selecta_test1,
        genre = self.genre_test1,
        rank = 1,
    )
    artist_dj_test1 = self.artist_dj_test1

    self.label_test1 = Label.objects.create(
        name = 'Label test1',
    )
    label_test1 = self.label_test1

    self.producer_test1 = Producer.objects.create(
        name = 'prodcuer test1',
        label = self.label_test1,
    )
    producer_test1 = self.producer_test1

    self.mix_test1 = Mix.objects.create(
        name = 'mix name test1',
        dj = self.artist_dj_test1,
        genre = self.genre_test1,
    )
    mix_test1 = self.mix_test1

    self.track_test1 = Track.objects.create(
        name = 'track test1',
        prodcuer = self.producer_test1,
        featured_artists = self.artist_dj_test1,
        genre = self.genre_test1,
    )
    track_test1 = self.track_test1


    #Calendar Models
    self.calendarentry_event1 = CalendarEntry.objects.create(
        event_bol = True,
        event = self.event_test1_scheduled,
    )
    calendarentry_event1 = self.calendarentry_event1

    self.calendarentry_event2 = CalendarEntry.objects.create(
        event_bol = True,
        event = self.event_test2_finished,
    )
    calendarentry_event2 = self.calendarentry_event2

    self.calendarentry_mix1 = CalendarEntry.objects.create(
        mix_bol = True,
        mix = self.mix_test1,
        date = datetime.date(2022, 12, 16),
    )
    calendarentry_mix1 = self.calendarentry_mix1

    self.calendarentry_track1 = CalendarEntry.objects.create(
        track_bol = True,
        track = self.track_test1,
        date = datetime.date(2022, 12, 17),
    )
    calendarentry_track1 = self.calendarentry_track1


    # Gallery Models
    self.gallery_test1 = Gallery.objects.create(
        name = 'gallery Test1',
        event = event_test2_finished,
    )


    self.photo_gallery_test1 = Photo.objects.create(
        gallery = gallery_test1,
        photo = 'photo_gal_test1.jpg'
    )


    self.photo_gallery_test2 = Photo.objects.create(
        gallery = gallery_test1,
        photo = 'photo_gal_test2.jpg'
    )


    args = {
        gallery_test1 : self.gallery_test1,
        photo_gal_test1 : self.photo_gallery_test1,
        photo_gal_test2 : self.photo_gallery_test2,

    }
    return args
