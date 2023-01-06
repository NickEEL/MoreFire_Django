from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from datetime import datetime, date, timedelta
#from django.utils import timezone
import pytz
from pytz import timezone
from django.utils.safestring import mark_safe
import calendar
from calendar import HTMLCalendar
from .calendar import MFCalendar
from  .models import CalendarEntry
from itertools import chain
from .models import Photohome, Infohome, Links
from music.models import Mix, Track, Artist, Soundsystem, Studio
from mfevents.models import Event, Venue, EventCrew
from galleries.models import Gallery, Photo

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


# Create your views here.
def linksview(request):
    links_all = Links.objects.all()
    links_mf = Links.objects.filter(mflink=True)
    links_fb = Links.objects.filter(type_lnk='fb').exclude(mflink=True)
    links_twit = Links.objects.filter(type_lnk='twit').exclude(mflink=True)
    links_inst = Links.objects.filter(type_lnk='inst').exclude(mflink=True)
    links_other = Links.objects.filter(type_lnk='other').exclude(mflink=True)
    artists_all = Artist.objects.exclude(name='N/A')
    soundsystem_all = Soundsystem.objects.exclude(name='N/A').exclude(name='More Fire Sound')
    studio_all = Studio.objects.exclude(name='N/A')
    eventcrew_all = EventCrew.objects.exclude(name='N/A').exclude(name='More Fire')

    args = {
        'current_year': current_year_utc,
        'links': links_all,
        'links_mf': links_mf,
        'links_fb': links_fb,
        'links_twit': links_twit,
        'links_inst': links_inst,
        'links_other': links_other,
        'artists_all':  artists_all,
        'soundsystem_all': soundsystem_all,
        'studio_all': studio_all,
        'eventcrew_all': eventcrew_all,
    }

    return render(request, 'home/links.html', args)


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request):
        photo_hm = Photohome.objects.all()
        photo_hm_1st_rdm = Photohome.objects.order_by('?').first()
        info_hm_1st = Infohome.objects.first()

        args = {
            'current_year': current_year_utc,
            'photo_hm': photo_hm_1st_rdm,
            'info_hm': info_hm_1st,
        }
        return render(request, self.template_name, args)


def basearg(request):


    args = {
        'current_year': current_year_utc,
    }
    return render(request, 'base.html', args )



def hmcalendar(request, year=current_year_utc, month=current_month_utc):
    mf_entries = CalendarEntry.objects.order_by('date').filter(
        date__year=year, date__month=month).exclude(event__status='Plan').exclude(event__status='Cancelled', event__finished=True )

    cal = MFCalendar(mf_entries).formatmonth(year, month)

    #Previous & Next month calculation
    cal_month_name_lst = list(calendar.month_name)
    d = datetime.now(tz_uk)


    #Previous
    first = d.replace(day=1)
    prev_month_last_day = first - timedelta(days=1)
    prev_month_num = prev_month_last_day.month
    prev_month = cal_month_name_lst[prev_month_num]
    prev_month_year_num = prev_month_last_day.year
    #Next
    days_in_month = calendar.monthrange(d.year, d.month)[1] # returns the number of days in the specified month.
    last = d.replace(day=days_in_month)
    next_month_day = last + timedelta(days=1)
    next_month_num = next_month_day.month
    next_month = cal_month_name_lst[next_month_num]
    next_month_year_num = next_month_day.year

    args = {
        'current_year': current_year_utc,
        'calendar': mark_safe(cal),
        'prev_month': prev_month,
        'prev_month_year': prev_month_year_num,
        'next_month': next_month,
        'next_month_year': next_month_year_num,
    }
    return render(request,'home/calendar.html', args)





def hmcalendarchangeview(request, year, month):
    #variables
    month = month.capitalize()
    month_number = int(list(calendar.month_name).index(month))
    month_number = int(month_number)

    #Current datetime info
    now = datetime.now(tz_uk)
    # Get current year
    current_year = now.year
    # current month
    current_month = now.month
    # current day
    current_day = now.day
    # Get current time
    current_time = now.strftime('%I:%M %p on %d.%m.%Y. %Z')

    #More Fire Events
    mf_entries = CalendarEntry.objects.order_by('date').filter(
        date__year=year, date__month=month_number).exclude(event__status='Plan').exclude(event__status='Cancelled', event__finished=True )

    cal = MFCalendar(mf_entries).formatmonth(year, month_number)

    # Previous & Next month calculation
    cal_month_name_lst = list(calendar.month_name)

    d = date(year=year, month=month_number, day=15)

    # Previous
    first = d.replace(day=1)
    prev_month_last_day = first - timedelta(days=1)
    prev_month_num = prev_month_last_day.month
    prev_month = cal_month_name_lst[prev_month_num]
    prev_month_year_num = prev_month_last_day.year
    # Next
    days_in_month = calendar.monthrange(d.year, d.month)[1]  # returns the number of days in the specified month.
    last = d.replace(day=days_in_month)
    next_month_day = last + timedelta(days=1)
    next_month_num = next_month_day.month
    next_month = cal_month_name_lst[next_month_num]
    next_month_year_num = next_month_day.year

    #arguments for template
    args = {
        'year':year,
        'month':month,
        'month_number':month_number,
        'current_year': current_year,
        'current_month': current_month,
        'current_day': current_day,
        'current_time': current_time,
        'mf_entries': mf_entries,
        'calendar': mark_safe(cal),
        'prev_month': prev_month,
        'prev_month_year': prev_month_year_num,
        'next_month': next_month,
        'next_month_year': next_month_year_num,
    }
    return render(request, 'home/calendar_change.html', args)



def site_search(request):
    #Check if events have finished
    events_list_all = Event.objects.all()
    for e in events_list_all:
        if e.finish_dt < now_utc:
            e.finished = True
            e.save()

    if request.method == "POST":
        searched = request.POST['searched']
        #Q query expressions
        events_q = Q(name__contains=searched) | Q(venue__name__contains=searched) | Q(selectas__name__contains=searched) | Q(vocals__name__contains=searched) | Q(instrumentals__name__contains=searched) | Q(genre__name__contains=searched)
        mix_q = Q(name__contains=searched) | Q(dj__name__contains=searched) | Q(featured_artists__name__contains=searched) | Q(genre__name__contains=searched)
        track_q = Q(name__contains=searched) | Q(producer__name__contains=searched) | Q(featured_artists__name__contains=searched) | Q(label__name__contains=searched) | Q(studio__name__contains=searched) | Q(genre__name__contains=searched)
        galleries_q = Q(name__contains=searched) | Q(event__name__contains=searched)

        #Search filters
        listings_srch = Event.objects.filter(events_q).exclude(status='Plan').exclude(finished=True).order_by('start_dt').distinct()
        past_events_srch = Event.objects.filter(events_q).exclude(status='Plan').exclude(finished=False).order_by('start_dt').distinct()
        mix_srch = Mix.objects.filter(mix_q).order_by('release_date').distinct()
        track_srch = Track.objects.filter(track_q).order_by('release_date').distinct()
        galleries_srch = Gallery.objects.filter(galleries_q).order_by('created_dt').distinct()


        args = {
            'current_year': current_year_utc,
            'searched': searched,
            'listings_srch': listings_srch,
            'past_events_srch': past_events_srch,
            'mix_srch': mix_srch,
            'track_srch': track_srch,
            'galleries_srch': galleries_srch,

        }
        return render(request, 'home/site_search.html', args)
    else:
        return render(request, 'home/site_search.html')
