from django.test import TestCase
from home.models import *
from music.models import *
from mfevents.models import *
from home.calendar import MFCalendar
from datetime import datetime, date, timedelta
from django.utils.timezone import make_aware

class TestHomeModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.genre_test1 = Genre.objects.create(
            name = 'genre test1',
        )
        cls.artist_type_selecta_test1 = ArtistType.objects.create(
            name = 'artist type selecta test1',
            selecta = True,
        )
        cls.artist_dj_test1 = Artist.objects.create(
            name = 'artist dj test1',
            rank = 1,
        )
        cls.artist_dj_test1.genre.add(cls.genre_test1)
        cls.artist_dj_test1.artist_type.add(cls.artist_type_selecta_test1)

        cls.soundsystem_test1 = Soundsystem.objects.create(
            name = 'soundsystem test1',
            rank = 1,
        )
        cls.soundsystem_test1.genre.add(cls.genre_test1)


        cls.group_test1 = Group.objects.create(
            name = 'group test1',

        )
        cls.group_test1.genre.add(cls.genre_test1)

        cls.studio_test1 = Studio.objects.create(
            name = 'studio test1',
        )

        cls.label_test1 = Label.objects.create(
            name = 'Label test1',
        )

        cls.producer_test1 = Producer.objects.create(
            name = 'prodcuer test1',
        )
        cls.producer_test1.label.add(cls.label_test1)

        cls.mix_test1 = Mix.objects.create(
            name = 'mix name test1',
            dj = cls.artist_dj_test1,
        )
        cls.mix_test1.genre.add(cls.genre_test1)

        cls.track_test1 = Track.objects.create(
            name = 'track test1',
            producer = cls.producer_test1,
        )
        cls.track_test1.genre.add(cls.genre_test1)
        cls.track_test1.featured_artists.add(cls.artist_dj_test1)


        cls.venue_test1 = Venue.objects.create(
            name = 'test venue1',
        )
        cls.eventcrew_test1 = EventCrew.objects.create(
            name = 'testcrew1',
        )
        cls.event_test1_scheduled = Event.objects.create(
            name = 'event test1',
            organiser = cls.eventcrew_test1,
            venue = cls.venue_test1,
            status = 'Scheduled',
            start_dt = make_aware(datetime.utcnow()) + timedelta(days=10),
            finish_dt = make_aware(datetime.utcnow()) + timedelta(days=10) + timedelta(hours=10),
            finished = False,
        )
        cls.event_test1_scheduled.genre.add(cls.genre_test1)
        cls.event_test1_scheduled.save()

        cls.links_test1 = Links.objects.create(
            name = 'link name test1',
            link_url = 'www.linktest1.net',
        )

        cls.cal_entry_event_test1 = CalendarEntry.objects.get(
            event_bol = True,
            event = cls.event_test1_scheduled,
        )
        cls.cal_entry_mix_test1 = CalendarEntry.objects.get(
            mix_bol = True,
            mix = cls.mix_test1,
        )
        cls.cal_entry_track_test1 = CalendarEntry.objects.get(
            track_bol = True,
            track = cls.track_test1,
        )

    def test_links_model_str(self):
        self.assertEqual(str(self.links_test1), "link name test1")

    def test_calendarentry_model_str(self):
        self.assertEqual(str(self.cal_entry_event_test1), "Event")
        self.assertEqual(str(self.cal_entry_mix_test1), "Mix")
        self.assertEqual(str(self.cal_entry_track_test1), "Track")

    def test_calendarentry_model_start_date(self):
        self.assertEqual(self.cal_entry_event_test1.start_date, self.event_test1_scheduled.start_dt)
        self.assertEqual(self.cal_entry_mix_test1.start_date, date.today())
        self.assertEqual(self.cal_entry_track_test1.start_date, date.today())

    def test_calendarentry_model_finish_date(self):
        self.assertEqual(self.cal_entry_event_test1.finish_date, self.event_test1_scheduled.finish_dt)
        self.assertEqual(self.cal_entry_mix_test1.finish_date, date.today())
        self.assertEqual(self.cal_entry_track_test1.finish_date, date.today())

    def test_calendarentry_model_get_absolute_url(self):
        event_test = self.cal_entry_event_test1
        mix_test = self.cal_entry_mix_test1
        track_test = self.cal_entry_track_test1

        self.assertEqual( '/events/event/1', event_test.get_absolute_url())
        self.assertEqual( '/music/mixes/1', mix_test.get_absolute_url())
        self.assertEqual( '/music/tracks/1', track_test.get_absolute_url())
