from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Category,self).save(*args, **kwargs)


class Post(models.Model):

    author = models.ForeignKey(User,limit_choices_to={'is_staff': True})
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='blog/posts',blank=True)
    thumbnail = models.ImageField(upload_to='blog/posts',blank=True)
    content = MarkdownField()
    summary = models.TextField()
    updatedAt =  models.DateTimeField('date modified',auto_now=True)
    createdAt =  models.DateTimeField('date published',auto_now_add=True)
    category = models.ManyToManyField(Category)

    class Meta:
	    verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Post,self).save(*args, **kwargs)

    def next(self):
        try:
            return get_object_or_404(Post,pk=self.pk+1)
        except:
            return None

    def previous(self):
        try :
            return get_object_or_404(Post,pk=self.pk-1)
        except:
            return None
