from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password


# The User Model for the UserCredentias Table
class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

# The Client Model for the ClientInformation Table
# UserCredentials and ClientInformation are one-to-one
class Client (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, default=None)
    stAddress1 = models.CharField(max_length = 100)
    stAddress2 = models.CharField(max_length = 100, blank=True)
    city = models.CharField(max_length = 100)
    STATES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hamphire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'), 
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'), 
    ]
    state = models.CharField(max_length = 2, choices=STATES)
    name = models.CharField(max_length = 50)
    zip = models.CharField(max_length = 9)
    def __str__(self):
        return self.name



<<<<<<< HEAD
class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)



class fuelQuote (models.Model):
    #gallonsRequested = models.CharField(max_length = 100)
    gallonsRequested = models.IntegerField()
    deliveryDate = models.DateField() 

    #hardcoded
    deliveryAddress = models.CharField(max_length = 100)
    suggestedPrice = models.DecimalField(max_digits = 100, decimal_places = 2)
    totalAmountDue = models.DecimalField(max_digits = 100, decimal_places = 2)
    #suggestedPrice = models.CharField(max_length = 100)
    #totalAmountDue = models.CharField(max_length = 100)
=======


>>>>>>> e265f6f71540306fa09efe7c756303204fdcd907
    