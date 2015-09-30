from django.db import models
from django.utils import timezone
from datetime import datetime





class News(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    unpublished = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=True,)

    def save(self):
        if self.published_date < timezone.now() and self.unpublished > timezone.now():
            self.is_published = True
        super(News, self).save()
    
    def __str__(self):
        return self.title

    





    
