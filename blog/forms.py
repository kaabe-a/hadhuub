from django import forms
from . models import Comment, Post,Category
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 30}))
    class Meta:
        model= Post
        fields = ['title','slug','thumbnail','body','category','tags']
       

class AdminForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['title',"slug",'body','category','status','tags','thumbnail']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['title']