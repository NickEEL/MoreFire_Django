from django.test import TestCase
from galleries.models import *
from mfevents.models import *
from datetime import datetime, date, timedelta
from django.utils.timezone import make_aware

class TestGalleriesModels(TestCase):

    def setUp(self):
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
            status = 'Finished',
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
            photo = 'photo_gal_test1.jpg'
        )


    def test_gallery_model_str(self):
        gal_test_id = self.gallery_test1.id
        gal_test_name = self.gallery_test1

        print(str(gal_test_name))
        print(str(gal_test_id))

        self.assertEqual(str(gal_test_name), "gallery Test1")

    def test_photo_model_get_absolute_url(self):
        photo_test = self.photo_gallery_test1
        print(photo_test.id)
        print(photo_test.gallery)
        print(photo_test.gallery.id)

        self.assertEqual( '/1/1/', photo_test.get_absolute_url())
