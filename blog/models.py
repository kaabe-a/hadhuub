from django.urls import reverse
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Category(models.Model):
    title = models.CharField(max_length=255) 
    
    def __str__(self) -> str:
        return self.title
    
STATUS_CHOICE_DRAFT = 'D'
STATUS_CHOICE_PUBLISH = 'P'
STATUS_CHOICES = [
   
    (STATUS_CHOICE_DRAFT, 'Drafted'),
    (STATUS_CHOICE_PUBLISH, 'Published'),
]

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    body = models.TextField(blank=True,null=True)
    status = models.CharField(
        max_length=56, choices=STATUS_CHOICES, default=STATUS_CHOICE_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='likes')
    like_count = models.PositiveBigIntegerField(default=0)
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='favorites')
    tags = TaggableManager()
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering=('-updated_at',)
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})
    
    
    def save(self,*args,**kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    @property
    def get_image_url(self):
        if self.image_url != '':
            return self.image_url
        else:
            return ""
    
class Comment(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(max_length=2,choices=STATUS_CHOICES,default=STATUS_CHOICE_DRAFT)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title