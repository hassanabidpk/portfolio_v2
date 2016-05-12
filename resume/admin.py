from django.contrib import admin
from .models import Skill,Project
from django_markdown.admin import AdminMarkdownWidget


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {'description':{'widget': AdminMarkdownWidget}}


admin.site.register(Skill)
admin.site.register(Project,ProjectAdmin)
