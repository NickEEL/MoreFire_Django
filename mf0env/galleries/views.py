from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator

from .models import Gallery, Photo


# Get current year
now = timezone.now()
current_year = now.year

# Create your views here.
def galleries(request):

    photo_galleries = Gallery.objects.all()

    # pagination
    p = Paginator(photo_galleries, 10)
    page = request.GET.get('page')
    photo_galleries_page = p.get_page(page)
    nums = "p" * photo_galleries_page.paginator.num_pages


    args = {
        'current_year': current_year,
        'photo_galleries': photo_galleries,
        'photo_galleries_page': photo_galleries_page,
        'nums': nums,

    }
    return render(request, 'galleries/galleries.html', args)



def gallery(request, gallery_id):
    photo_gallery = Gallery.objects.get(pk=gallery_id)
    photos = Photo.objects.filter(gallery__id=gallery_id)

    args = {
        'current_year': current_year,
        'photo_gallery': photo_gallery,
        'photos': photos,
    }
    return render(request, 'galleries/gallery.html', args)



def photo(request, gallery_id , photo_id):
    photo = Photo.objects.get(pk=photo_id)
    photos = Photo.objects.filter(gallery__id=gallery_id)
    photos_count = photos.count
    gallery = Gallery.objects.get(pk=gallery_id)

    # pagination.  This method does not work to go through whole gallery from this page.
    p = Paginator(photos, 1)
    page = request.GET.get('page')
    photos_page = p.get_page(page)
    nums = "p" * photos_page.paginator.num_pages

    args = {
        'current_year': current_year,
        'photo': photo,
        'photos': photos,
        'photos_page': photos_page,
        'nums': nums,
        'gallery': gallery,
    }
    return render(request, 'galleries/photo.html', args)
