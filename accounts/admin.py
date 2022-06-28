from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import Follow, User,Profile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email", "password1", "password2","first_name","last_name"),
            },
        ),
    )
    
# @admin.register(Profile)
# class Profi    

admin.site.register(Profile)
admin.site.register(Follow)