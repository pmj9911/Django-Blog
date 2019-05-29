from django import forms
from . import models

class CreateProfile(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['First_Name', 'Last_Name', 'Email_Address', 'Age', 'Profile_Pic']

class UpdateProfile(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['First_Name', 'Last_Name', 'Email_Address', 'Age', 'Profile_Pic']