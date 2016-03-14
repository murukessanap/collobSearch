from django.db import models
from django.contrib.postgres.fields import JSONField
#from django.utils import timezone


class Searcher(models.Model):
    #author = models.ForeignKey('auth.User')
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    areaOfInterest = models.CharField(max_length=20)
    expertise = models.IntegerField()
    urls = JSONField(default=dict)

    def publish(self):
        expertise = 0
        self.save()

    def __str__(self):
        return self.username
