from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb =  models.ImageField(upload_to='images/',default='images/default.png',blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    document = models.FileField(upload_to='documents/',default='default.txt')         
    def __str__(self):
        return self.title


    def snippet(self):
    	return self.body[:250]

    def delete(self, *args, **kwargs):
        self.thumb.delete()
        self.document.delete()
        super().delete(*args, **kwargs)