from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import News

def index(request):
    latest_news_list = News.objects.order_by('-pub_date')[:5]
    context = {'latest_news_list': latest_news_list}
    return render(request, 'posts/index.html', context)

def detail(request, news_id):
    return HttpResponse("You're looking at story %s." % news_id)
    question = get_object_or_404(News, pk=news_id)
    return render(request, 'posts/detail.html', {'news': news})

