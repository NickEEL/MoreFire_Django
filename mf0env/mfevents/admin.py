from django.contrib import admin
from .models import Venue, Event, EventEnquiry,EventCrew

# Register your models here.
@admin.register(EventCrew)
class EventCrewAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )
#admin.site.register(EventCrew)  'contact_name',


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'postcode','website', 'contact_email')
    ordering = ('name', 'postcode')
#admin.site.register(Venue)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'finished' ,'status','type', 'venue', 'start_dt')
    ordering = ('-start_dt', )# negative date reverses order in admin list.
#admin.site.register(Event)


@admin.register(EventEnquiry)
class EventEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    ordering = ('created_dt',)
#admin.site.register(EventEnquiry)
