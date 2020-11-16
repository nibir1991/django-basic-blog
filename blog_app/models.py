from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=100)
    def __str__ (self):
        return self.name 


    def get_absolute_url(self):
        return reverse('home')

class profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True, blank=True, upload_to= 'images/profile')
    website_url=models.CharField(max_length=255,null=True, blank=True)
    facebook_url=models.CharField(max_length=255,null=True, blank=True)
    linkdin_url=models.CharField(max_length=255,null=True, blank=True)
    twitter_url=models.CharField(max_length=255,null=True, blank=True)

    def __str__ (self):
        return str(self.user) 


class post(models.Model):

    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=255)
    post_body=RichTextField(blank=True,null=True)
    post_thumb=models.ImageField(null=True, blank=True, upload_to= 'images/')
    post_date=models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    snippet=models.CharField(max_length=255)
    def __str__ (self):
        return self.title + '|'+str(self.author)+'|'+str(self.post_date)+'|'+str (self.post_body)+'|'+str(self.post_thumb)  

    def total_likes(self):
        return self.likes.count()
        
    def get_absolute_url(self):
        return reverse('home')
        
class comment(models.Model):
    post=models.ForeignKey(post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body=models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return '%s - %s' % (self.post.title, self.name)

