from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,related_name="profile")
	pic = models.ImageField(upload_to="profile",default="profile.png", blank=True, null=True)
	location = models.CharField(max_length=200, null=True, blank=True,default="")
	bio = models.TextField(max_length=200, null=True, blank=True, default="Hello, I am a new user! ")
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.user.username