from django.contrib import admin

from .models import CalendarEntry, Photohome , Infohome, Links

# Register your models here.
admin.site.register(CalendarEntry)
admin.site.register(Photohome)
admin.site.register(Infohome)
admin.site.register(Links)