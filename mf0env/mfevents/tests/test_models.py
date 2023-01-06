from django.test import TestCase
from mfevents.models import *
from music.models import Genre
from datetime import datetime, date, timedelta
from django.utils.timezone import make_aware

class TestMFEventsModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.genre_test1 = Genre.objects.create(
            name = 'genre test1',
        )
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

        cls.event_test2_finished = Event.objects.create(
            name = 'event test2',
            organiser = cls.eventcrew_test1,
            venue = cls.venue_test1,
            status = 'Finished',
            start_dt = make_aware(datetime.utcnow()) - timedelta(days=10),
            finish_dt = make_aware(datetime.utcnow()) + timedelta(hours=10) - timedelta(days=10),
            finished = True,
        )
        cls.eventenquiry_test1 = EventEnquiry.objects.create(
            name = 'enquiry name test1',
            email = 'test1@email.com',
            phone = '01234123456',
            message = 'this is a message test1 text.',
        )


    def test_eventcrew_model_str(self):
        self.assertEqual(str(self.eventcrew_test1), "testcrew1")

    def test_venue_model_str(self):
        self.assertEqual(str(self.venue_test1), "test venue1")

    def test_eventenquiry_model_str(self):
        self.assertEqual(str(self.eventenquiry_test1), "enquiry name test1")

    def test_event_test1_model_str(self):
        self.assertEqual(str(self.event_test1_scheduled), "event test1")

    def test_event_test1_days_until(self):
        self.assertEqual(self.event_test1_scheduled.days_until, "10")

    def test_event_test1_days_until(self):
        self.assertEqual(self.event_test2_finished.days_until, "-10 days")

    def test_event_get_absolute_url(self):
        self.event_test1 = Event.objects.get(id=1)

        self.assertEqual( '/events/event/1', self.event_test1.get_absolute_url())
