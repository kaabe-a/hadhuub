from django.contrib import admin
from blog.models import Category, Post,Comment
from . forms import AdminForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = AdminForm
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
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body','created_at')
    list_filter = ('status','created_at')
    list_per_page = 10

    # def save_model(self, request, obj, form, change) -> None:
    #     obj.user = request.user
    #     return super().save_model(request, obj, form, change)