from django.contrib import admin

from apps.blog.models import Blog, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')



class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'blog')  # Add the fields you want to display in the list view

admin.site.register(Comment, CommentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
