from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'datetime_created')

admin.site.register(Post, PostAdmin)

