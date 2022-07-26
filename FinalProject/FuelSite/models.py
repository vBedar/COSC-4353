from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password


# The User Model for the UserCredentias Table
class User(models.Model):
    username = models.CharField(max_length=15, unique=True) #Added unique constraint as a user with the same username and password might bringg up the wring ID ~ Victoria
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


class fuelQuote (models.Model):
    #gallonsRequested = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE) #I added a foreign key for this model as it's a many-to-one relationship ~Victoria
    gallonsRequested = models.PositiveIntegerField() #Changed the field to one that only accepts positive values ~ Victoria
    deliveryDate = models.DateField() #Will need an extra validation to make sure the delivery date isn't in the past ~ Victoria

    #hardcoded
    deliveryAddress = models.CharField(max_length = 100)
    suggestedPrice = models.DecimalField(max_digits = 100, decimal_places = 2)
    totalAmountDue = models.DecimalField(max_digits = 100, decimal_places = 2)
    #suggestedPrice = models.CharField(max_length = 100)
    #totalAmountDue = models.CharField(max_length = 100)

    #Total Price module 
    def get_total_price(self):
        #Margin = currentprice(1.50) * (location(in or out of state) - history factor(client has history) + gallons requested(over or under 1000) + company profit (10%))
        currentprice = 1.50
        companyProfit = .1
        if self.deliveryAddress == 'TX' # not sure how to single out the state yet maybe have the delivery address be composed of 3 different fields? ~ Victoria
            location = .02
        else
            location = .04

        #A way to determine if the client has history probably by quereing the foreign key

        if self.gallonsRequested > 1000
            gallonFactor = .02
        else
            gallonFactor = .03

        margin = (location - history + gallonFactor + companyProfit)*currentprice
        self.suggestedPrice = currentprice + margin
        self.totalAmountDue = self.gallonsRequested*self.suggestedPrice

    