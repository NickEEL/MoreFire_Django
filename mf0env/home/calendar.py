from calendar import HTMLCalendar
from datetime import datetime, date
from itertools import groupby
#from django.utils import timezone
from django.utils.html import conditional_escape as esc
from .models import Event
from django.db import models


#More Fire events
class MFCalendar(HTMLCalendar):

    def __init__(self, mfentries):
        super(MFCalendar, self).__init__()
        self.mfentries = self.group_by_day(mfentries)

    def formatday(self, day: int, weekday: int) -> str:
        if day !=0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += '_today'
            if day in self.mfentries:
                cssclass += '_filled'
                body = ['<ul>']
                for mfentries in self.mfentries[day]:
                    body.append('<li>')
                    body.append('<a href="%s">' % mfentries.get_absolute_url())
                    body.append(esc(mfentries))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '-')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(MFCalendar, self).formatmonth(year, month)

    def group_by_day(self, mfentries):
        field = lambda mfentry: mfentry.date.day
        return dict(
            [(day, list(items)) for day, items in groupby(mfentries, field)],
            )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)