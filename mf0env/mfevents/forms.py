from django import forms
from django.forms import ModelForm
from .models import EventEnquiry
from captcha.fields import CaptchaField

# Create an Event Enquiry form
class EventEnquiryForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = EventEnquiry
        fields = ('name','email','phone','message')
        labels = {
            'name':'',
            'email':'',
            'phone':'',
            'message':'',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name.' }),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your email address.'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your phone (optional).'}),
            'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter details of your enquiry here please.'}),
        }