from dataclasses import fields
from urllib import request
from django import forms
from . models import Comment, Post,Category
from django_summernote.fields import SummernoteTextField,SummernoteWidget
from django_summernote.widgets import SummernoteInplaceWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}))
    class Meta:
        model= Post
        fields = ['title','slug','body','category','tags']
       

class AdminForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['title',"slug",'body','category','status','tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','title','body']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['title']