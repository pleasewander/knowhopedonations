from knowhope.model.models import Donation

def getDonationPercentage():
    donations = Donation.objects.all()
    total = 0
    percentage = 0

    for donatee in donations:
        total += donatee.amount

    percentage = total / 7000
    percentage = percentage * 100

    return percentage

def getDonateeList():
    donations = Donation.objects.all().order_by('name')
    donatees = []

    for donatee in donations:
        donatees.append(donatee.name)

    return donatees