from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from collobSearch.models import KeyVal
from collobSearch.models import UrlMap
from collobSearch.models import Searcher
from .forms import LoginForm

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
    searchers=Searcher.objects.all()
    for s in searchers:
        data[s.username]=[]
        urlMaps=UrlMap.objects.filter(searcher=s)
        for um in urlMaps:
            urls=KeyVal.objects.filter(urlmap=um)
            for u in urls:
                data[s.username].append((um.areaOfInterest,u.url))
    #print(data)
    #searchers=Searcher.objects.all()
    return render(request, 'collobSearch/index.html', {'data':data})

def index(request):
    #return render(request, 'collobSearch/failure.html', {})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            if Searcher.objects.get(username=form.username):
              return render(request, 'collobSearch/success.html', {'form':form})
            else:
              return render(request, 'collobSearch/failure.html', {'form':form})
    else:
        form = LoginForm()
    return render(request, 'collobSearch/login.html', {'form':form})


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('collobSearch/login.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def main(request):
    return HttpResponseRedirect('/urls/')