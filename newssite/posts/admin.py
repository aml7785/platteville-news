from django.contrib import admin

# Register your models here.
from .models import News


class NewsAdmin(admin.ModelAdmin):
    fields = ['news_text', 'pub_date', 'unpub_date']

admin.site.register(News, NewsAdmin)






