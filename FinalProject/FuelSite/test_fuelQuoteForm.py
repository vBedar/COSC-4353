from django.test import TestCase
from FuelSite.models import fuelQuote, User, Client
from FuelSite.forms import fuelQuoteForm
from django.urls import reverse, resolve
from FuelSite.views import fuelQuoteComplete, submitFuelQuote
from django.utils import timezone

import datetime
import decimal

# Create your tests here.
class fuelQuoteTestCase(TestCase):
    
    def setUp(self):
        #User Models
        use1 = User.objects.create(username="use1", password="1234")
        use2 = User.objects.create(username="use2", password="1234")


        #Valid forms
        fuelQuote.objects.create(user=use1, gallonsRequested= "5", deliveryDate ="2022-08-29", deliveryAddress="5555 yes street", suggestedPrice= "50.35", totalAmountDue= "150.39")
        fuelQuote.objects.create(user=use2, gallonsRequested= "24", deliveryDate ="2022-09-14", deliveryAddress="9999 no street", suggestedPrice= "90.21", totalAmountDue= "270.54")
    
    def testfuelQuoteForm(self):
        #Form with gallons requested not numeric
        formOne = fuelQuoteForm(data = {'gallons_requested':"five", 'delivery_date':"2022-08-29", 'delivery_address':"5555 yes street", 'suggested_price':"50.35", 'total_amount_due':"150"})
        self.assertFalse(formOne.is_valid())

        #Form with incorrect delivery date format
        formTwo = fuelQuoteForm(data = {'gallons_requested':"5", 'delivery_date':"29-2022-08", 'delivery_address':"5555 yes street", 'suggested_price':"50.00", 'total_amount_due':"150.00"})
        self.assertFalse(formTwo.is_valid())

        #Form with delivery date far in the future
        formThree = fuelQuoteForm(data = {'gallons_requested':"5", 'delivery_date':"2026-08-29", 'delivery_address':"5555 yes street", 'suggested_price':"50.53", 'total_amount_due':"150.24"})
        self.assertTrue(formThree.is_valid())

    def test_fq_validity_model(self):
        #Valid forms
        user1 = fuelQuote.objects.get(id=1)
        user2 = fuelQuote.objects.get(id=2)

        #gallonsRequested
        self.assertEqual(user1.gallonsRequested, 5) 
        self.assertEqual(user2.gallonsRequested, 24)
        #deliveryDate
        self.assertEqual(user1.deliveryDate, datetime.date(2022, 8, 29))
        self.assertEqual(user2.deliveryDate, datetime.date(2022, 9, 14))
        #deliveryAddress
        self.assertEqual(user1.deliveryAddress, "5555 yes street")
        self.assertEqual(user2.deliveryAddress, "9999 no street")
        #suggestedPrice
        self.assertEqual(user1.suggestedPrice, decimal.Decimal('50.35'))
        self.assertEqual(user2.suggestedPrice, decimal.Decimal('90.21'))
        #totalAmountDue
        self.assertEqual(user1.totalAmountDue, decimal.Decimal('150.39'))
        self.assertEqual(user2.totalAmountDue, decimal.Decimal('270.54'))
    
    def test_completeurl(self):
        compresponse = self.client.get('/1/quote/complete/')
        self.assertEqual(compresponse.status_code, 200)
        
    # def test_template(self):
    #     tempresponse = self.client.get('/1/quote/')
    #     self.assertEqual(tempresponse.status_code, 200)
    #     self.assertTemplateUsed(tempresponse, 'FuelQuoteForm.html')


    # def test_list_url_resolves(self):
    #     url = reverse (fuelQuoteComplete)
    #     self.assertEquals(resolve(url).func,fuelQuoteComplete)

    # def test_list_url_resolves(self):
    #     url = reverse (submitFuelQuote)
    #     self.assertEquals(resolve(url).func,submitFuelQuote)
