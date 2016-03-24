from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from collobSearch.models import KeyVal
from collobSearch.models import UrlMap
#from collobSearch.models import Searcher
from accounts.models import User
from .forms import LoginForm
import google

@login_required(login_url='/')
def urlList(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #urls=KeyVal.objects.all()
    '''data=[]
    searchers=Searcher.objects.all()
    for s in searchers:
        urlMaps=UrlMap.objects.filter(searcher=s)
        for um in urlMaps:
            urls=KeyVal.objects.filter(urlmap=um)
            for u in urls:
                data.append((s.username,um.areaOfInterest,u.url))'''
    data={}
    searchers=User.objects.all()
    for s in searchers:
        data[s.email]=[]
        urlMaps=UrlMap.objects.filter(searcher=s)
        for um in urlMaps:
            urls=KeyVal.objects.filter(urlmap=um)
            for u in urls:
                data[s.email].append((um.areaOfInterest,u.url))
    #print(data)
    #searchers=Searcher.objects.all()
    return render(request, 'collobSearch/index.html', {'data':data})


@login_required(login_url='/')
def searchQuery(request):
    return render(request, 'collobSearch/gsearch.html', {})

@login_required(login_url='/')
def googleList(request):
    urls=[]
    query=""
    if request.POST:
        query=request.POST.get("query", "")
    count=50
    i=0
    for url in google.search(query):
        urls.append(url)
        i=i+1
        if count==i:
          break
    return render(request, 'collobSearch/gresult.html', {'urls':urls})

def index(request):
    #return render(request, 'collobSearch/failure.html', {})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            if User.objects.get(email=form.email):
              return render(request, 'collobSearch/success.html', {'form':form})
            else:
              return render(request, 'collobSearch/failure.html', {'form':form})
    else:
        form = LoginForm()
    return render(request, 'collobSearch/login.html', {'form':form})


def login_user(request):
    logout(request)
    email = password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect('/main/')
                return HttpResponseRedirect('/search/')
    return render_to_response('collobSearch/login.html', context_instance=RequestContext(request))

'''@login_required(login_url='/')
def main(request):
    str=""
    if request.POST:
        str=request.POST.get("query", "")
    return HttpResponseRedirect('/g',{'str':str})'''
