from django.contrib import admin
#from .models import Searcher
from .models import UrlMap
from .models import KeyVal

admin.site.register(UrlMap)
admin.site.register(KeyVal)
#admin.site.register(Searcher)

