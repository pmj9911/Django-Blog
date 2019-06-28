from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer
from django.core.paginator import Paginator


def article_list(request):
    article = Article.objects.all().order_by('date')

    page = request.GET.get('page', 1)

    paginator = Paginator(article, 3)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)



    return render(request, 'ArticlesApp/articles_list.html',{'articles':articles})

@login_required(login_url="/accounts/login/")
def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'ArticlesApp/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
	if request.method == "POST" :
		form = forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('ArticlesApp:list')			
	else:
		form = forms.CreateArticle()
	return render(request, 'ArticlesApp/article_create.html',{'form':form})

@login_required(login_url="/accounts/login/")
def article_delete(request, pk):
	if request.method == "POST":
		article = Article.objects.get(pk=pk)
		article.delete()
	return redirect('ArticlesApp:list')

@login_required(login_url="/accounts/login/")
def article_update(request,slug):
	instance = Article.objects.get(slug=slug)
	if request.method == 'POST':
		form = forms.UpdateArticle(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			instance2 = Article.objects.get(slug=slug)
			return render(request, 'ArticlesApp/article_detail.html', {'article':instance2 })
	else:
		form = forms.UpdateArticle(instance=instance)
	return render(request, 'ArticlesApp/article_update.html', {'form':form , 'article':instance})

class ArticlesList(APIView):
	def get(self,request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)