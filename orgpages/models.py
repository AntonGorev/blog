from tinymce import HTMLField
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Orgpage(models.Model):
    title = models.CharField(max_length=100)
    #alias = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    #overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)
    #thumbnail = models.ImageField()
    #categories = models.ManyToManyField(Category)
    #featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={
            'slug': self.slug
        })
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Orgpage, self).save(*args, **kwargs)
"""
    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })
"""
