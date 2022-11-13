from django.urls import path
from . import views
from .views import galleries, gallery

urlpatterns = [
    path('', views.galleries, name='galleries'),
    path('gallery/<int:gallery_id>/', views.gallery, name='gallery'),
    path('<int:gallery_id>/<int:photo_id>/', views.photo, name='photo'),
]

