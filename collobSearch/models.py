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

    def __iter__(self):
        #return [field.value_to_string(self) for field in Searcher._meta.fields]
        self.count = 0 
        self.list =  [ self.username, 
                       self.password, 
                       self.areaOfInterest, 
                       self.expertise ] 
        return self

    def __next__(self):
      if self.count == len(self.list):
        raise StopIteration
      self.count = self.count + 1
      return self.list[self.count - 1]

class UrlMap(models.Model):
    areaOfInterest  = models.CharField(max_length=50)
    username = models.ForeignKey(Searcher, db_index=True, null=True) 

    def publish(self):
        self.save()

    def __str__(self):
        return "UrlMap"

    def __iter__(self):
        #return [field.value_to_string(self) for field in UrlMap._meta.fields]
        self.count = 0
        self.list = [ self.areaOfInterest, 
                       self.username ] 
        return self

    def __next__(self):
      if self.count == len(self.list):
        raise StopIteration
      self.count = self.count + 1
      return self.list[self.count - 1]

class KeyVal(models.Model):
    aoi = models.ForeignKey(UrlMap, db_index=True)
    url = models.CharField(max_length=240, db_index=True)

    def publish(self):
        self.save()

    def __str__(self):
        return "KeyVal"
    
    def __iter__(self):
        #return [field.value_to_string(self) for field in KeyVal._meta.fields]
        self.count = 0
        self.list = [ self.aoi,
                      self.url ]
        return self

    def __next__(self):
      if self.count == len(self.list):
        raise StopIteration
      self.count = self.count + 1
      return self.list[self.count - 1]
