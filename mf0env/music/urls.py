from django.urls import path
from . import views

urlpatterns = [
    #path arguments ('url', view.function, (optional args) name of page)

    path('mixes/', views.music_mixes ,name='mixes'),
    path('tracks/', views.music_tracks ,name='tracks'),
    path('mixes/<mix_id>', views.music_mix_profile ,name='mix-profile'),
    path('tracks/<track_id>', views.music_track_profile ,name='track_profile'),

]