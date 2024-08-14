from django.contrib import admin
from parler.admin import TranslatableAdmin 
from .models import BlogPost 

@admin.register(BlogPost) 
class BlogPostAdmin(TranslatableAdmin):
    list_display = ('title', 'created_at')