from django.contrib import admin
from .models import Category,Post
from django_markdown.admin import AdminMarkdownWidget


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {'content':{'widget': AdminMarkdownWidget}}


admin.site.register(Category)
admin.site.register(Post,PostAdmin)
