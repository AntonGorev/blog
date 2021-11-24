from django.contrib import admin

from .models import Album, Image

class ImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
 
    class Meta:
       model = Album
 
@admin.register(Image)
class PostImageAdmin(admin.ModelAdmin):
    pass