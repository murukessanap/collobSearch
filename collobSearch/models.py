from django.db import models
#from django.contrib.postgres.fields import JSONField
#from django.utils import timezone

class Searcher(models.Model):
    #author = models.ForeignKey('auth.User')
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    areaOfInterest = models.CharField(max_length=50)
    expertise = models.IntegerField()
    #urlmap = models.ForeignKey(UrlMap,null=True, db_index=True)

    def publish(self):
        expertise = 0
        self.save()

    def __str__(self):
        return self.username

class UrlMap(models.Model):
    areaOfInterest  = models.CharField(max_length=50)
    username = models.ForeignKey(Searcher, db_index=True, null=True) 
    def publish(self):
        self.save()

    def __str__(self):
        return self.username+','+self.areaOfInterest

class KeyVal(models.Model):
    aoi = models.ForeignKey(UrlMap, db_index=True)
    url = models.CharField(max_length=240, db_index=True)

    def publish(self):
        self.save()
