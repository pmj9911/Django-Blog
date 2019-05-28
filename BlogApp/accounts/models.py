from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	Username = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
	First_Name = models.CharField(max_length=100)
	Last_Name = models.CharField(max_length=100)
	email = models.EmailField()
	linker = models.CharField(max_length=100, null=True)

	#Date_Of_Birth = models.DateTimeField()
	Profile_Pic =  models.ImageField(upload_to='ProfilePics/',default='ProfilePics/default.jpg',blank=True)    

	def __str__(self):
		return self.First_Name + " " + self.Last_Name

	def delete(self, *args, **kwargs):
		self.Profile_Pic.delete()
		super().delete(*args, **kwargs)