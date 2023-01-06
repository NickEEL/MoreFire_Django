from django.test import TestCase, Client
from django.urls import reverse
from music.models import *

class TestViews(TestCase):

    """docstring forTestViews.TestCase """

    def setUp(self):
        self.client = Client()
        self.music_mixes_url = reverse('mixes')
        self.music_tracks_url = reverse('tracks')
        self.music_mix_profile_url = reverse('mix-profile', args=[1])
        self.music_track_profile_url = reverse('track_profile', args=[1])
        self.genre_test1 = Genre.objects.create(
            name = 'genre test1',
        )
        self.artist_type_selecta_test1 = ArtistType.objects.create(
            name = 'selecta test1',
            selecta = True,
        )

        self.artist_dj_test1 = Artist.objects.create(
            name = 'artist dj test1',
            #artist_type = self.artist_type_selecta_test1,
            #genre = self.genre_test1,
            rank = 1,
        )
        self.label_test1 = Label.objects.create(
            name = 'Label test1',
        )
        self.producer_test1 = Producer.objects.create(
            name = 'prodcuer test1',
            #label = self.label_test1,
        )
        self.mix_test1 = Mix.objects.create(
            name = 'mix name test1',
            dj = self.artist_dj_test1,
            #genre = self.genre_test1,
        )
        self.track_test1 = Track.objects.create(
            name = 'track test1',
            producer = self.producer_test1,
            #featured_artists = self.artist_dj_test1,
            #genre = self.genre_test1,
        )
        #set many to manay objects with add funvtions
        self.artist_dj_test1.artist_type.add(self.artist_type_selecta_test1)
        self.artist_dj_test1.genre.add(self.genre_test1)
        self.producer_test1.label.add(self.label_test1)
        self.mix_test1.genre.add(self.genre_test1)
        self.track_test1.genre.add(self.genre_test1)
        self.track_test1.featured_artists.add(self.artist_dj_test1)

    def test_music_mixes_GET(self):
        response = self.client.get(self.music_mixes_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/music_mixes.html')


    def test_music_tracks_GET(self):

        response = self.client.get(self.music_tracks_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/music_tracks.html')


    def test_music_mix_profile_GET(self):
        response = self.client.get(self.music_mix_profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/music_mix_profile.html')


    def test_music_track_profile_GET(self):
        response = self.client.get(self.music_track_profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/music_track_profile.html')
