from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'ArticlesApp/articles_list.html',{'articles':articles})

def article_detail(request,slug):
	#return HttpResponse(slug)	
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

def article_delete(request, pk):
	if request.method == "POST":
		article = Article.objects.get(pk=pk)
		article.delete()
	return redirect('ArticlesApp:list')

class ArticlesList(APIView):
	def get(self,request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)