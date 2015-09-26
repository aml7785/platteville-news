from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices
from django.utils import timezone
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManager
from datetime import datetime

class PostQuerySet(QuerySet):
    def by_author(self, user):
        return self.filter(user=user)

    def published(self):
        return self.filter(published_date__lte=datetime.now())

    def unpublished(self):
        return self.filter(published_date__gte=datetime.now())

# Create your models here.
class News(models.Model):
    STATUS = Choices('draft', 'published')
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    unpublish_date = models.DateTimeField(blank=True, null=True)
    objects = PassThroughManager(PostQuerySet)
    status = StatusField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

News.objects.published()
News.objects.unpublished()

    
