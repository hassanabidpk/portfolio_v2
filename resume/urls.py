from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^contact/thanks/$',views.contact_thanks,name='contact_thanks'),

]
