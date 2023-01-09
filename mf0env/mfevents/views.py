from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator
import calendar
from calendar import HTMLCalendar
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from .models import Event, EventEnquiry
from music.models import Track
from .forms import EventEnquiryForm
from galleries.models import Gallery, Photo


# Create your views here.

#global variables
tz_uk = timezone('Europe/London')
tz_utc = pytz.utc
now_utc = datetime.now(timezone(tz_utc.zone))

current_year_utc = now_utc.year
# current month
current_month_utc = now_utc.month
# current day
current_day_utc = now_utc.day
# Get current time
current_time_utc = now_utc.strftime('%I:%M %p on %d.%m.%Y. %Z')
# Get current year

def event_profile(request, event_id):
    event = Event.objects.get(pk=event_id)
    event_start = event.start_dt.astimezone(tz_uk).strftime('%I:%M %p on %d.%m.%Y. %Z')
    event_finish = event.finish_dt.astimezone(tz_uk).strftime('%I:%M %p on %d.%m.%Y. %Z')
    selectas = event.selectas.exclude(name='N/A')
    vocals = event.vocals.exclude(name='N/A')
    instrumentals = event.instrumentals.exclude(name='N/A')
    venue_url = event.venue.website

    selectas_vl = event.selectas.exclude(name='N/A').values_list('name', flat=True)
    vocals_vl = event.vocals.exclude(name='N/A').values_list('name', flat=True)
    instrumentals_vl = event.instrumentals.exclude(name='N/A').values_list('name', flat=True)
    event_artists_lst_zip = zip(selectas_vl, vocals_vl, instrumentals_vl)
    gall = Gallery.objects.all()
    e_gals = gall.filter(event__id= event_id)

    args = {
        'event':event,
        'event_start': event_start,
        'event_finish': event_finish,
        'selectas': selectas,
        'vocals': vocals,
        'instrumentals': instrumentals,
        'venue_url': venue_url,
        'selectas_vl': selectas_vl,
        'vocals_vl': vocals_vl,
        'instrumentals_vl': instrumentals_vl,
        'artists_zip': event_artists_lst_zip,
        'event_galleries': e_gals,
        'current_year': current_year_utc,
    }

    return render(request, 'mfevents/event_profile.html', args )


def event_enquiry(request):
    submitted = False
    if request.method == "POST":
        form = EventEnquiryForm(request.POST)
        if form.is_valid():
            human = True
            form.save()
            return HttpResponseRedirect(reverse('enquiry-success'))

    else:
        form = EventEnquiryForm
        if 'submitted' in request.GET:
            submitted = True

    args = {
        'form': form,
        'submitted': submitted,
        'current_year': current_year_utc,
    }

    return render(request, 'mfevents/event_enquiry.html', args)




def enquiry_success(request):
    enq = EventEnquiry.objects.last()

    # send an email
    send_mail(
        'More Fire Enquiry-' + enq.name,  # subject
        enq.message, # message
        enq.email, # from email
        ['morefireproductions@email.com'], #To email
    )

    args = {
        'current_year': current_year_utc,
    }

    return render(request, 'mfevents/event_enquiry_success.html', args)



def events_list(request):
    events_list_all = Event.objects.all()
    for e in events_list_all:
        if e.finish_dt < now_utc:
            e.finished = True
            e.save()

    events_list = Event.objects.exclude(status='Plan').exclude(finished=True).order_by('start_dt')
    events_list_count = events_list.count()

    # pagination
    p = Paginator(events_list, 3)
    page = request.GET.get('page')
    events_list_page = p.get_page(page)
    nums = "p" * events_list_page.paginator.num_pages

    args = {
        'events_list': events_list,
        'events_list_count': events_list_count,
        'events_list_page': events_list_page,
        'nums': nums,
        'current_year': current_year_utc,
    }
    return render(request, 'mfevents/event_list.html', args)


def past_events_list(request):
    events_list_all = Event.objects.all()
    for e in events_list_all:
        if e.finish_dt < now_utc:
            e.event_finished = True
            e.save()

    events_list_past = Event.objects.filter(finished=True).filter(status='Scheduled').order_by('-finish_dt')
    events_list_past_count = events_list_past.count()

    # pagination
    p = Paginator(events_list_past, 5)
    page = request.GET.get('page')
    events_list_past_page = p.get_page(page)
    nums = "p" * events_list_past_page.paginator.num_pages

    args = {
        'events_list_past': events_list_past,
        'events_list_past_count': events_list_past_count,
        'events_list_past_page': events_list_past_page,
        'nums': nums,
        'current_year': current_year_utc,
    }
    return render(request, 'mfevents/past_event_list.html', args)
