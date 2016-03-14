from django.db import models
#from django.contrib.postgres.fields import JSONField
#from django.utils import timezone

class UrlMap(models.Model):
    areaOfInterest      = models.CharField(max_length=50)

class KeyVal(models.Model):
    aoi = models.ForeignKey(UrlMap, db_index=True)
    url     = models.CharField(max_length=240, db_index=True)


class Searcher(models.Model):
    #author = models.ForeignKey('auth.User')
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    areaOfInterest = models.CharField(max_length=50)
    expertise = models.IntegerField()
    urls = UrlMap()

    def publish(self):
        expertise = 0
        self.save()

    def __str__(self):
        return self.username
