from django.conf.urls import patterns, url
from django.shortcuts import render,render_to_response
from knowhope.donationsdao import getDonationPercentage
from models import donation

def mainpage(request):
    totalPercentage = getDonationPercentage()
    template = {
        'totalPercentage' : totalPercentage,
    }
    return render_to_response('home.html', template)

def donationsuccess(request):
    donatee= request.POST.get('first_name')
    donationammount = request.POST.get('payment_gross')

    newdonation = donation(name = donatee, amount = donationammount)
    newdonation.save()

    return request

urlpatterns = patterns('knowhope.appController',
            url(r'^', mainpage),
            url(r'^/success', donationsuccess)
)