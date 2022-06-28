from django.contrib import admin
from blog.models import Category, Post,Comment
from . forms import PostForm
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    form = PostForm
    summernote_fields = ('body',)
    list_display = ['title','category_title','status']
    list_filter = ('created_at','updated_at','status')
    list_editable  = ('status',)
    prepopulated_fields = {'slug':['title']}
    
    search_fields = ('title',)
    autocomplete_fields = ['category']
    list_select_related = ['category']
    list_per_page = 10
    
    def category_title(self,post):
        return post.category.title

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    search_fields = ['title']
    list_per_page = 10
    

admin.site.register(Comment)
