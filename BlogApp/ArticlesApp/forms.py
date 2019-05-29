from django import forms
from . import models

class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title', 'body', 'slug', 'thumb',  'document']


class UpdateArticle(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title', 'body', 'thumb',  'document']	