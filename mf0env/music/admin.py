from django.contrib import admin
from .models import Artist, ArtistType, Genre, Group, Producer, Soundsystem, Track, Mix, Label

# Register your models here.
admin.site.register(ArtistType)
admin.site.register(Genre)
admin.site.register(Group)
admin.site.register(Label)
admin.site.register(Producer)
admin.site.register(Soundsystem)




@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name','email' )
    ordering = ('name',)
#admin.site.register(Artist)

@admin.register(Mix)
class MixAdmin(admin.ModelAdmin):
    list_display = ('name','dj','release_date' )
    ordering = ('release_date', 'name' )
#admin.site.register(Mix)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name','release_date' )
    ordering = ('release_date', 'name')
#admin.site.register(Track)