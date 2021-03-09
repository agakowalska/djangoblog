from django.contrib import admin

from . models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'pub_date', 'author', 'category']
    list_filter = ['pub_date', 'author', 'category']
    date_hierarchy = 'pub_date'
    search_fields = ['post_title', 'author', 'pub_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


