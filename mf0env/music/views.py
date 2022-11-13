from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator

from .models import Artist, Label, Mix, Track

# Create your views here.
def music_mix_profile(request, mix_id):
    mix_profile = Mix.objects.get(pk=mix_id)
    feat_artists = mix_profile.featured_artists.exclude(name='N/A')
    genre = mix_profile.genre.exclude(name='N/A')

    args = {
        'mix_profile': mix_profile,
        'feat_artists': feat_artists,
        'genre': genre,
    }
    return render(request, 'music/music_mix_profile.html', args)


def music_track_profile(request, track_id):
    track_profile = Track.objects.get(pk=track_id)
    feat_artists = track_profile.featured_artists.exclude(name='N/A')
    genre = track_profile.genre.exclude(name='N/A')


    args = {
        'track_profile': track_profile,
        'feat_artists': feat_artists,
        'genre': genre,
    }
    return render(request, 'music/music_track_profile.html', args)

def music_mixes(request):
    now = timezone.now()
    current_year = now.year
    mix_list_all= Mix.objects.all().order_by('-release_date')


    # pagination
    p = Paginator(mix_list_all, 5)
    page = request.GET.get('page')
    mix_list_page = p.get_page(page)
    nums = "p" * mix_list_page.paginator.num_pages

    args = {
        'mix_list_all': mix_list_all,
        'mix_list_page': mix_list_page,
        'nums': nums,
        'current_year': current_year,
    }

    return render(request, 'music/music_mixes.html', args)


def music_tracks(request):
    now = timezone.now()
    current_year = now.year
    track_list_all = Track.objects.all().order_by('-release_date')

    # pagination
    p = Paginator(track_list_all, 5)
    page = request.GET.get('page')
    track_list_page = p.get_page(page)
    nums = "p" * track_list_page.paginator.num_pages

    args = {
        'track_list_all': track_list_all,
        'track_list_page': track_list_page,
        'nums': nums,
        'current_year': current_year,
    }

    return render(request, 'music/music_tracks.html', args)