from django.test import TestCase, Client
from django.urls import reverse
from galleries.models import *
from mfevents.models import *
from datetime import datetime, date, timedelta
from django.utils.timezone import make_aware


class TestViews(TestCase):

    """docstring forTestViews.TestCase """

    def setUp(self):
        self.client = Client()
        self.galleries_url = reverse('galleries')
        self.gallery_url = reverse('gallery', args=[1])
        self.photo_url = reverse('photo', args=[1, 1])
        self.venue_test1 = Venue.objects.create(
            name = 'test venue1',
        )
        self.eventcrew_test1 = EventCrew.objects.create(
            name = 'testcrew1',
        )
        self.event_test2_finished = Event.objects.create(
            name = 'event test2',
            organiser = self.eventcrew_test1,
            venue = self.venue_test1,
            status = 'Scheduled',
            start_dt = make_aware(datetime.utcnow()) - timedelta(days=10),
            finish_dt = make_aware(datetime.utcnow()) + timedelta(hours=10) - timedelta(days=10),
            finished = True,
        )
        self.gallery_test1 = Gallery.objects.create(
            name = 'gallery Test1',
            event = self.event_test2_finished,
        )
        self.photo_gallery_test1 = Photo.objects.create(
            gallery = self.gallery_test1,
            photo = 'photo_gal_test1.jpg',
        )


    def test_galleries_GET(self):
        response = self.client.get(self.galleries_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'galleries/galleries.html')


    def test_gallery_GET(self):
        response = self.client.get(self.gallery_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'galleries/gallery.html')


    def test_photo_GET(self):
        response = self.client.get(self.photo_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'galleries/photo.html')
