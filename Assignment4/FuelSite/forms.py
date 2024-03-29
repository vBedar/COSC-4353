from django import forms
from django.utils import timezone

class clientForm(forms.Form):
    full_name = forms.CharField(label = "Enter your full name", max_length = 50)
    address_1 = forms.CharField(label = "Enter your primary steert address", max_length = 100)
    address_2 = forms.CharField(label = "Enter your secondary steert address", max_length = 100, required = False)
    city = forms.CharField(label = "Enter your city", max_length = 100)
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
    state = forms.ChoiceField(label = "Select your state", choices = STATELIST)
    zipcode = forms.CharField(label = "Enter Your ZipCode", max_length = 9, min_length = 5)




class fuelQuoteForm(forms.Form):
    #gallons_requested = forms.CharField(initial= "10", required=False)
    gallons_requested = forms.IntegerField()
    delivery_date = forms.DateField(initial= timezone.now)

    #hardcoded

    delivery_address = forms.CharField(initial= "333666 assignment street", required=False)
    suggested_price = forms.DecimalField(initial= "23.50", max_digits = 100, decimal_places = 2)
    total_amount_due = forms.DecimalField(initial= "55.50", max_digits = 100, decimal_places = 2)
    #suggested_price = forms.CharField(initial= "25.50", required=False)
    #total_amount_due = forms.CharField(initial= "50.50", required=False)