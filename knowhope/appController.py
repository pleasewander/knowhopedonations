from django.conf.urls import patterns, url
from django.shortcuts import render,render_to_response, redirect
from knowhope.donationsdao import getDonationPercentage, getDonateeList
from knowhope.model.models import Donation

def mainpage(request):
    totalPercentage = getDonationPercentage()
    template = {
        'totalPercentage' : totalPercentage,
    }
    return render(request, 'home.html', template)

def donationoptions(request):
    return render(request, 'donations.html')

def donationsuccess(request):
    donatee= request.POST.get('first_name')
    donationammount = request.POST.get('mc_gross1')
    if donationammount == 0 or donationammount == None:
        donationammount = request.POST.get('mc_gross')

    if donatee == None:
        donatee = ' '

    newdonation = Donation(name = donatee, amount = donationammount)
    newdonation.save()

    return redirect('/')

def donatees(request):
    donations = Donation.objects.all()
    donatees = getDonateeList()

    template = {
        'donatees' : donatees,
    }

    return render(request, 'donatees.html', template)

urlpatterns = patterns('knowhope.appController',
            url(r'^$', mainpage),
            url(r'^donations$', donationoptions),
            url(r'^paypal$', donationsuccess),
            url(r'^donatees$', donatees),
)