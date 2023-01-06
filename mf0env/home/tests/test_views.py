from django.test import TestCase, Client
from django.urls import reverse
from home.models import *

class TestViews(TestCase):

    """docstring forTestViews.TestCase """

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.home_calendar_url = reverse('home_calendar')
        self.hmcalendarchangeview_url = reverse('calendar_ym', args=[2022, 'April'])
        self.site_search_url = reverse('search-site')
        self.links_url = reverse('links')


    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


    def test_hmcalendar_GET(self):
        response = self.client.get(self.home_calendar_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/calendar.html')


    def test_hmcalendarchangeview_GET(self):
        response = self.client.get(self.hmcalendarchangeview_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/calendar_change.html')


    def test_site_search_GET(self):
        response = self.client.get(self.site_search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/site_search.html')


    def test_links_GET(self):
        response = self.client.get(self.links_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/links.html')
