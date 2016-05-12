from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField


class Skill(models.Model):

	title = models.CharField(max_length=250)
	logo = models.ImageField(upload_to='resume/skills',blank=True)
	term = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		return super(Skill,self).save(*args, **kwargs)

class Project(models.Model):

    title = models.CharField(max_length=300)
    description = MarkdownField()
    github_link = models.URLField(max_length=300,blank=True)
    android = models.URLField(max_length=300,blank=True)
    ios = models.URLField(max_length=300,blank=True)
    web = models.URLField(max_length=300,blank = True)
    skills  = models.ManyToManyField(Skill)
    author = models.ForeignKey(User,limit_choices_to={'is_staff': True})
    image = models.ImageField(upload_to='resume/projects',blank=True)
    slug = models.SlugField(max_length=120, unique=True)
    updatedAt =  models.DateTimeField(auto_now=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Project,self).save(*args, **kwargs)
