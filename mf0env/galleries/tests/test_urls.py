from django.test import SimpleTestCase
from django.urls import reverse, resolve
from galleries.views import *

class TestUrls(SimpleTestCase):

    def test_galleries_url_is_resolved(self):
        url = reverse('galleries')
        self.assertEquals(resolve(url).func, galleries)


    def test_gallery_url_is_resolved(self):
        url = reverse('gallery', args=[1])
        self.assertEquals(resolve(url).func, gallery)


    def test_photo_url_is_resolved(self):
        url = reverse('photo', args=[1, 101])
        self.assertEquals(resolve(url).func, photo)







"""
    def test_assert(self):
        assert 1==2
"""
