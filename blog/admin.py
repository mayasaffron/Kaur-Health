from django.contrib import admin
from .models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)

