from django.test import SimpleTestCase
from django.urls import reverse, resolve
from music.views import *

class TestUrls(SimpleTestCase):

    def test_music_mixes_url_is_resolved(self):
        url = reverse('mixes')
        self.assertEquals(resolve(url).func, music_mixes)
        print(resolve(url))

    def test_music_tracks_url_is_resolved(self):
        url = reverse('tracks')
        self.assertEquals(resolve(url).func, music_tracks)
        print(resolve(url))

    def test_music_mix_profile_url_is_resolved(self):
        url = reverse('mix-profile', args=[1])
        self.assertEquals(resolve(url).func, music_mix_profile)
        print(resolve(url))

    def test_music_track_profile_url_is_resolved(self):
        url = reverse('track_profile', args=[2])
        self.assertEquals(resolve(url).func, music_track_profile)
        print(resolve(url))





"""
    def test_assert(self):
        assert 1==2
"""
