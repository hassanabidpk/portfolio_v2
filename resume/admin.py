from django.contrib import admin
from .models import Skill,Project
from django_markdown.admin import AdminMarkdownWidget

class SkillAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {'description':{'widget': AdminMarkdownWidget}}
    exclude = ('slug',)

admin.site.register(Skill,SkillAdmin)
admin.site.register(Project,ProjectAdmin)
