from django.shortcuts import render
from .models import Article
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'ArticlesApp/articles_list.html',{'articles':articles})