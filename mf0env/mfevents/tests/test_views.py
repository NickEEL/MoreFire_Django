from django.test import TestCase, Client
from django.urls import reverse
from mfevents.models import *
from datetime import datetime, date, timedelta
from django.utils.timezone import make_aware

class TestViews(TestCase):

    """docstring forTestViews.TestCase """

    def setUp(self):
        self.client = Client()
        self.events_list_url = reverse('events-list')
        self.past_events_list_url = reverse('past-events-list')
        self.event_enquiry_url = reverse('enquiries')
        self.enquiry_success_url = reverse('enquiry-success')
        self.event_profile_url = reverse('event-profile', args=[1])
        self.genre_test1 = Genre.objects.create(
            name = 'genre test1',
        )
        self.venue_test1 = Venue.objects.create(
            name = 'test venue1',
        )
        self.eventcrew_test1 = EventCrew.objects.create(
            name = 'testcrew1',
        )
        self.event_test1_scheduled = Event.objects.create(
            name = 'event test1',
            organiser = self.eventcrew_test1,
            venue = self.venue_test1,
            status = 'Scheduled',
            start_dt = make_aware(datetime.utcnow()),
            finish_dt = make_aware(datetime.utcnow()) + timedelta(hours=10) ,
            finished = False,
            #genre = self.genre_test1,
        )
        self.event_test1_scheduled.genre.add(self.genre_test1)


    def test_events_list_GET(self):
        response = self.client.get(self.events_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mfevents/event_list.html')


    def test_past_events_list_GET(self):
        response = self.client.get(self.past_events_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mfevents/past_event_list.html')


    def test_event_enquiry_GET(self):
        response = self.client.get(self.event_enquiry_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mfevents/event_enquiry.html')


    def test_enquiry_success_GET(self):
        response = self.client.get(self.enquiry_success_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mfevents/event_enquiry_success.html')


    def test_event_profile_GET(self):
        response = self.client.get(self.event_profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mfevents/event_profile.html')
