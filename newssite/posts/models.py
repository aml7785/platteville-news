from django.db import models
from django.utils import timezone

class News(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    news_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    unpub_date = models.DateTimeField('date to unpublish', null=True, blank=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




    

        
  
    


    
