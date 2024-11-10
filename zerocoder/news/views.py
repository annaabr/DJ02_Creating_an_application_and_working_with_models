from django.shortcuts import render
from .models import News_post
from .models import News_post_HW

# Create your views here.
def home(request):
    news = News_post.objects.all()
    news_HW = News_post_HW.objects.all()
    data = {
        'news': news,
        'news_HW': news_HW
    }
    return render(request, 'news/news.html', data)