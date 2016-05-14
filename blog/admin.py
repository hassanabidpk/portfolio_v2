from django.contrib import admin
from .models import Category,Post
from django_markdown.admin import AdminMarkdownWidget


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'createdAt')
    formfield_overrides = {'content':{'widget': AdminMarkdownWidget}}
    exclude = ('slug',)


admin.site.register(Category)
admin.site.register(Post,PostAdmin)
