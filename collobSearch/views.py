from django.http import HttpResponse
from django.shortcuts import render
from collobSearch.models import KeyVal
from collobSearch.models import UrlMap
from collobSearch.models import Searcher


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #urls=KeyVal.objects.all()
    data=[]
    searchers=Searcher.objects.all()
    for s in searchers:
        urlMaps=UrlMap.objects.filter(searcher=s)
        for um in urlMaps:
            urls=KeyVal.objects.filter(urlmap=um)
            for u in urls:
                data.append((s.username,um.areaOfInterest,u.url))
    #print(data)
    #searchers=Searcher.objects.all()
    return render(request, 'collobSearch/index.html', {'data':data})
