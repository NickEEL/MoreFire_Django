from django.urls import path
from . import views


urlpatterns = [
    #path arguments ('url', view.function, (optional args) name of page)

    path('listings/', views.events_list, name='events-list'),
    path('past_events/', views.past_events_list, name='past-events-list'),
    path('enquiries/', views.event_enquiry, name='enquiries'),
    path('enquiry_success/', views.enquiry_success, name='enquiry-success'),
    path('event/<event_id>', views.event_profile, name='event-profile'),



]