from django.db import models

# Create your models here.
class fuelQuote (models.Model):
    gallonsRequested = models.IntegerField()
    deliveryDate = models.DateField() 

    #hardcoded
    deliveryAddress = models.CharField(max_length = 100)
    suggestedPrice = models.DecimalField(max_digits = 100, decimal_places = 2)
    totalAmountDue = models.DecimalField(max_digits = 100, decimal_places = 2)