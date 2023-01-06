from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import linksview, HomeView, hmcalendar, hmcalendarchangeview, site_search

class TestUrls(SimpleTestCase):

    def test_HomeView_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)


    def test_linksview_url_is_resolved(self):
        url = reverse('links')
        self.assertEquals(resolve(url).func, linksview)


    def test_hmcalendar_url_is_resolved(self):
        url = reverse('home_calendar')
        self.assertEquals(resolve(url).func, hmcalendar)


    def test_hmcalendarchangeview_url_is_resolved(self):
        url = reverse('calendar_ym', args=[2022, 'December'])
        self.assertEquals(resolve(url).func, hmcalendarchangeview)


    def test_site_search_url_is_resolved(self):
        url = reverse('search-site')
        self.assertEquals(resolve(url).func, site_search)
        








"""
    def test_assert(self):
        assert 1==2
"""
