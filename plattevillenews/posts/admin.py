from django.contrib import admin
from .models import News
import reversion

# Register your models here.
class NewsAdmin(reversion.VersionAdmin):
    readonly_fields = ('created_date', 'modified_date',)
    pass
    


    
admin.site.register(News, NewsAdmin)


