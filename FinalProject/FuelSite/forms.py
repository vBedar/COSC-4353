from django import forms
from django.utils import timezone
from .models import Client


class clientForm(forms.Form):
    full_name = forms.CharField(label = "Enter your full name", max_length = 50, initial = "")
    address_1 = forms.CharField(label = "Enter your primary street address", max_length = 100, initial = "")
    address_2 = forms.CharField(label = "Enter your secondary street address", max_length = 100, required = False, initial="")
    city = forms.CharField(label = "Enter your city", max_length = 100, initial="")
    STATELIST = [
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
    state = forms.ChoiceField(label = "Select your state", choices = STATELIST, initial = "TX")
    zipcode = forms.CharField(label = "Enter Your ZipCode", max_length = 9, min_length = 5, initial = "")





class fuelQuoteForm(forms.Form):
    gallons_requested = forms.IntegerField()
    delivery_date = forms.DateField(initial= timezone.now, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    #delivery_address = forms.CharField(initial= )

    #hardcoded
    
    #suggested_price = forms.DecimalField(initial= "0", max_digits = 100, decimal_places = 2, required= False, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #total_amount_due = forms.DecimalField(initial= "0", max_digits = 100, decimal_places = 2, required= False, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #suggested_price = forms.CharField(initial= "25.50", required=False)
    #total_amount_due = forms.CharField(initial= "50.50", required=False)

    def get_total_price(self):
        #Margin = currentprice(1.50) * (location(in or out of state) - history factor(client has history) + gallons requested(over or under 1000) + company profit (10%))
        currentprice = 1.50
        companyProfit = .10
        if self.deliveryAddress.find('TX') != -1: # not sure how to single out the state yet maybe have the delivery address be composed of 3 different fields? ~ Victoria
            location = .02
        else:
            location = .04

        #A way to determine if the client has history probably by quereing the foreign key
        count = fuelQuote.objects.filter(user=self.user).count()
        if count > 1:
            history = .01
        else:
            history = 0
    
        if self.gallonsRequested > 1000:
            gallonFactor = .02
        else:
            gallonFactor = .03

        margin = (location - history + gallonFactor + companyProfit)*currentprice
        self.suggestedPrice = round(currentprice + margin, 2)
        self.totalAmountDue = round(self.gallonsRequested*self.suggestedPrice, 2)