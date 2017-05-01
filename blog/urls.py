from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$', views.frontpage, name='index'),
    url(r'^/post/(?P<pk>\d+)/$', views.entry_detail, name='entry_detail'),
    url(r'^/post/new/$', views.entry_form, name='entry_form'),
]
