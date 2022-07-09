from django.contrib import admin
from blog.models import Category, Post,Comment
from . forms import AdminForm
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = AdminForm
    # summernote_fields = ('body',)
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
    
    def save_model(self, request, obj, form, change) -> None:
        obj.author = request.user
        return super().save_model(request, obj, form, change)
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    search_fields = ['title']
    list_per_page = 10
    

admin.site.register(Comment)
