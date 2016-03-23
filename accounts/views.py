from django.shortcuts import render
from .forms import AuthenticationForm
from .forms import RegistrationForm
from .models import User
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #if User.objects.get(email=user.email):   
            #  return HttpResponseRedirect('/accounts/failure/')
            #else:
            form.save()
            return HttpResponseRedirect('/')
        #else:
        #    return render(request, 'accounts/index.html', {'form':form})
    else:    
        form = RegistrationForm()
    return render(request, 'accounts/index.html', {'form':form})

def success(request):
    return render(request, 'accounts/success.html', {})

def failure(request):
    return render(request, 'accounts/failure.html', {})
