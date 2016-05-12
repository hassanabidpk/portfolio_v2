from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', views.post_single, name = 'post_single'),
    url(r'^category/(?P<slug>[-_\w]+)/$', views.posts_cat, name = 'posts_cat'),
    url(r'^$', views.index, name='index'),
]
