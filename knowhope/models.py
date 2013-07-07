from django.db import models

class donation(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
