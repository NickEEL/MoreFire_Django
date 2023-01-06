from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mfevents.views import *

class TestUrls(SimpleTestCase):

    def test_event_profile_url_is_resolved(self):
        url = reverse('event-profile', args=[1])
        self.assertEquals(resolve(url).func, event_profile)
        print(resolve(url))

    def test_event_enquiry_url_is_resolved(self):
        url = reverse('enquiries')
        self.assertEquals(resolve(url).func, event_enquiry)
        print(resolve(url))

    def test_enquiry_success_url_is_resolved(self):
        url = reverse('enquiry-success')
        self.assertEquals(resolve(url).func, enquiry_success)
        print(resolve(url))

    def test_events_list_url_is_resolved(self):
        url = reverse('events-list')
        self.assertEquals(resolve(url).func, events_list)
        print(resolve(url))

    def test_past_events_list_url_is_resolved(self):
        url = reverse('past-events-list')
        self.assertEquals(resolve(url).func, past_events_list)
        print(resolve(url))





"""
    def test_assert(self):
        assert 1==2
"""
