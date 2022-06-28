from django import forms
from . models import Comment, Post
from django_summernote.fields import SummernoteTextField,SummernoteWidget
from django_summernote.widgets import SummernoteInplaceWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}))
    class Meta:
        model= Post
        fields = ['title','slug','body','category','tags']
        # widgets = {
        #     'body':SummernoteInplaceWidget()
        # }
    # def clean_image_url(self):
    #     image_url = self.cleaned_data.get('image_url',False)
    #     print(image_url)
    #     valid_extensions = ['jpg', 'jpeg']
    #     extension = image_url.rsplit('.', 1)[1].lower()
    #     if extension not in valid_extensions:
    #         raise forms.ValidationError('The given URL does not match valid image extensions.')
    #     print(image_url)
    #     return image_url

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','title','body']