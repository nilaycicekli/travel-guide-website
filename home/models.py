from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model):
    title=models.CharField(max_length=200, null=True, blank=True,default="")
    body= models.TextField(max_length=200, null=True, blank=True, default="This is my first blog post!")
    pic = models.ImageField(upload_to="content",default="", blank=True, null=True)
    author= models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name="content")
    district=models.ForeignKey('District', null=True, on_delete=models.CASCADE,related_name="content")
    tag=models.ManyToManyField('Tag',  related_name="content", blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    likelist = models.ManyToManyField(User, blank=True, related_name="liked")
    savelist = models.ManyToManyField(User, blank=True, related_name="saved")

    def __str__(self):
        return self.title

class Comment(models.Model):
    rate=models.IntegerField(null=True,default=0)
    text=models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name="comment")
    content=models.ForeignKey('Content', null=True, on_delete=models.CASCADE,related_name="comment")

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True,default="")
   
    #MULTIPLE EKLE

    def __str__(self):
	    return self.name


class City(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True,default="")
    code=models.IntegerField()
    def __str__(self):
        return self.name



class District(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True,default="")
    city=models.ForeignKey('City', null=True, on_delete=models.CASCADE,related_name="district")
    def __str__(self):
        return self.name

