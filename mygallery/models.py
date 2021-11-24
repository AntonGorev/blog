from django.db import models

def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.name
    return f'{name}/images/{filename}'

class Album(models.Model):
    name = models.CharField(max_length=255)

class Image(models.Model):
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)