from django.conf.urls import url
from django.views.generic.dates import DateDetailView
from datetime import datetime
from dateutil import parser
from . import views
from .models import Entry

def datify(date_time_str):
    date_time = parser.parse(date_time_str)
    date_time = date_time.replace(tzinfo=None)
    received_datetime = datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')
    return received_datetime.date()

urlpatterns = [
    url(r'^/$', views.frontpage, name='frontpage'),
    url(r'^/post/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<pk>\d+)$', DateDetailView.as_view(model=Entry, date_field='pub_date', month_format=u'%m',), name='entry_detail'),
    #url(r'^/post/(?P<pk>\d+)/$', views.entry_detail, name='entry_detail'),
    url(r'^/post/new/$', views.entry_form, name='entry_form'),
]
