from django.conf.urls import patterns, url
from django.shortcuts import render


def mainpage(request):
    return render(request, 'home.html')

def donationsuccess(request):
    dun = request.POST

    return request

urlpatterns = patterns('knowhope.appController',
            url(r'^', mainpage),
            url(r'^/success', donationsuccess)
)