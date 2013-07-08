from knowhope.model.models import Donation

def getDonationPercentage():
    donations = Donation.objects.all()
    total = 0
    percentage = 0

    for donatee in donations:
        total += donatee.amount

    percentage = total / 7000
    percentage = total * 100

    return percentage
