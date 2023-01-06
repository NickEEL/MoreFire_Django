from django.test import SimpleTestCase
from mfevents.forms import EventEnquiryForm
from mfevents.models import EventEnquiry

class TestForms(SimpleTestCase):

    def setUp(self):
        self.form_data = {
            'name':'testname1',
            'email':'test1@test.com',
            'phone':'01234123456',
            'message':'this is a message test1 text.',
        }

"""
    def test_event_enquiry_form_valid_input(self):

        form = EventEnquiryForm(data=self.form_data)

        self.assertTrue(form.is_valid())


    def test_event_enquiry_form_not_valid_input(self):
        form = EventEnquiryForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
"""
