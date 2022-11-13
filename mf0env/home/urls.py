from django.urls import path
from . import views
from .views import HomeView, hmcalendarchangeview, hmcalendar, site_search, linksview


urlpatterns = [
    #path arguments ('url', view.function, (optional args) name of page)

    path('', HomeView.as_view(), name='home'),
    path('calendar/', views.hmcalendar, name='home_calendar'),
    path('calendar/<int:year>/<str:month>/', views.hmcalendarchangeview, name='calendar_ym'),
    path('search/', views.site_search, name='search-site'),
    path('links/', views.linksview, name='links'),

]