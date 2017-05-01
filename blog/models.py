from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Entry(models.Model):
    author = models.ForeignKey('auth.User',default='james')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    entry_body = models.TextField()