from django.conf.urls import patterns, url
from django.shortcuts import render,render_to_response
from knowhope.donationsdao import getDonationPercentage
from knowhope.model.models import Donation

def mainpage(request):
    totalPercentage = getDonationPercentage()
    template = {
        'totalPercentage' : totalPercentage,
    }
    return render(request, 'home.html', template)

def donationsuccess(request):
    donatee= request.POST.get('first_name')
    donationammount = request.POST.get('payment_gross')

    newdonation = Donation(name = donatee, amount = donationammount)
    newdonation.save()

    return request

urlpatterns = patterns('knowhope.appController',
            url(r'^', mainpage),
            url(r'^/success', donationsuccess)
)