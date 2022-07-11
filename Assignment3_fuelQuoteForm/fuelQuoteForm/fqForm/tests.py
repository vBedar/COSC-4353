from django.test import TestCase
from fqForm.models import fuelQuote
from fqForm.forms import fuelQuoteForm
from django.urls import reverse, resolve
from fqForm.views import index, fuelQuoteComplete, submitFuelQuote
# Create your tests here.
class fuelQuoteTestCase(TestCase):
    
    def setUp(self):
        #Valid forms
        fuelQuote.objects.create(gallonsRequested="5", deliveryDate ="8/29/2022", deliveryAddress="5555 yes street", suggestedPrice="50", totalAmountDue="150")
        fuelQuote.objects.create(gallonsRequested="9", deliveryDate ="9/14/2022", deliveryAddress="9999 no street", suggestedPrice="90", totalAmountDue="270")
    
    def testfuelQuoteForm(self):
        #Form with gallons requested not numeric
        formOne = fuelQuoteForm(data = {'gallons_requested':"five", 'delivery_date':"8/29/2022", 'delivery_address':"5555 yes street", suggested_price:"50", total_amount_due:"150"})
        self.assertFalse(formOne.is_valid())

        #Form with incorrect delivery date format
        formTwo = fuelQuoteForm(data = {'gallons_requested':"5", 'delivery_date':"29/2022/08", 'delivery_address':"5555 yes street", suggested_price:"50", total_amount_due:"150"})
        self.assertFalse(formTwo.is_valid())

        #Form with delivery date far in the future
        formThree = fuelQuoteForm(data = {'gallons_requested':"5", 'delivery_date':"8/29/2026", 'delivery_address':"5555 yes street", suggested_price:"50.535", total_amount_due:"150"})
        self.assertTrue(formThree.is_valid())

    def test_validity_model(self):
        #Valid forms
        five = fuelQuote.objects.get(deliveryAddress="5555 yes street")
        nine = fuelQuote.objects.get(deliveryAddress="9999 no street")

        self.assertEqual(five.gallonsRequested, "5") 
        self.assertEqual(nine.gallonsRequested, "9")

        self.assertEqual(five.deliveryDate, "8/29/2022")
        self.assertEqual(nine.deliveryDate, "9/14/2022")

        self.assertEqual(five.deliveryAddress, "5555 yes street")
        self.assertEqual(nine.deliveryAddress, "9999 no street")
    
    def test_template(self):
        tempresponse = self.client.get('/fuelQuoteForm/quote/')
        self.assertEqual(tempresponse.status_code, 200)
        self.assertTemplateUsed(tempresponse, 'fqForm/FuelQuoteForm.html')

    def test_completeurl(self):
        compresponse = self.client.get('/fuelQuoteForm/quote/complete/')
        self.assertEqual(compresponse.status_code, 200)

    def test_list_url_resolves(self):
        url = reverse (index)
        self.assertEquals(resolve(url).func,index)
    
    def test_list_url_resolves(self):
        url = reverse (fuelQuoteComplete)
        self.assertEquals(resolve(url).func,fuelQuoteComplete)

    def test_list_url_resolves(self):
        url = reverse (submitFuelQuote)
        self.assertEquals(resolve(url).func,submitFuelQuote)


            
