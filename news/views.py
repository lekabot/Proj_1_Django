from django.shortcuts import render
from .models import Articles

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_page.html', {'news': news})
def create(request):
    return render(request, 'news/create.html')