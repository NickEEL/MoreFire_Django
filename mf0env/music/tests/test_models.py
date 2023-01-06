from django.test import TestCase
from music.models import *
from mfevents.models import *
from datetime import datetime, date, timedelta
from django.utils.timezone import make_aware

class TestMusicModels(TestCase):

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


    def test_genre_model_str(self):
        self.assertEqual(str(self.genre_test1), "genre test1")

    def test_artist_type_model_str(self):
        self.assertEqual(str(self.artist_type_selecta_test1), "artist type selecta test1")

    def test_soundsystem_model_str(self):
        self.assertEqual(str(self.soundsystem_test1), "soundsystem test1")

    def test_label_model_str(self):
        self.assertEqual(str(self.label_test1), "Label test1")

    def test_group_model_str(self):
        self.assertEqual(str(self.group_test1), "group test1")

    def test_studio_model_str(self):
        self.assertEqual(str(self.studio_test1), "studio test1")

    def test_mix_model_str(self):
        self.assertEqual(str(self.mix_test1), "mix name test1")

    def test_track_model_str(self):
        self.assertEqual(str(self.track_test1), "track test1")
