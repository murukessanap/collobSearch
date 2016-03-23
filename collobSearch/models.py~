from django.db import models
#from django.contrib.postgres.fields import JSONField
#from django.utils import timezone

class Searcher(models.Model):
    #author = models.ForeignKey('auth.User')
    username = models.CharField(primary_key=True,max_length=20)
    password = models.CharField(max_length=20)
    areaOfInterest = models.CharField(max_length=50)
    expertise = models.IntegerField()
    #urlmap = models.ForeignKey(UrlMap,null=True, db_index=True)

    def publish(self):
        self.expertise = 0
        self.save()

    def __str__(self):
        return self.username


class UrlMap(models.Model):
    id = models.AutoField(primary_key=True)
    searcher = models.ForeignKey(Searcher, db_index=True)
    areaOfInterest  = models.CharField(max_length=50)

    class Meta:
        unique_together = (('searcher', 'areaOfInterest'),)

    def publish(self):
        self.save()

    def __str__(self):
        return self.areaOfInterest + str(self.id)



class KeyVal(models.Model):
    id = models.AutoField(primary_key=True)
    urlmap = models.ForeignKey(UrlMap, db_index=True)
    url = models.CharField(max_length=240)

    class Meta:
        unique_together = (('urlmap', 'url'),)

    def publish(self):
        self.save()

    def __str__(self):
        return self.url + str(self.id)

