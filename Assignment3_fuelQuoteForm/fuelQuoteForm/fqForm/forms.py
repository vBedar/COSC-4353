from django import forms

class fuelQuoteForm(forms.Form):
    gallons_requested = forms.IntegerField(required=False)
    delivery_date = forms.DateField(required=False)

    #hardcoded
    delivery_address = forms.CharField(initial= "333666 assignment street", required=False)
    suggested_price = forms.DecimalField(initial= 25, required=False)
    total_amount_due = forms.DecimalField(initial= 50, required=False)