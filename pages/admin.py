from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_posted')
    list_display_links = ('id', 'title')
    list_per_page = 20

admin.site.register(Post, PostAdmin)
