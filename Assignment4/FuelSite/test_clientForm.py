from django.test import TestCase
from FuelSite.models import Client, User
from FuelSite.forms import clientForm

# Create your tests here.
class ClientTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Users for the Client
        u1 = User.objects.create(username="user1", password="1234")
        u2 = User.objects.create(username="user2", password="1234")
        #Valid Client no 2nd address
        Client.objects.create(user=u1, name="Dave", stAddress1="3333 Nowhere st.", state="TX", city="Somewhere", zip="33333")
        #Valis Client with 2nd address
        Client.objects.create(user=u2, name="Betty", stAddress1="444 None ave.", stAddress2="3234 h bl.", state="AL", city="u", zip="7777")

    def testClientForm(self):
        #Form with no address 2
        form_Dave = clientForm(data = {'full_name':"Dave", 'address_1':"3333 Nowhere St.", 'state':"TX", 'city':"Somewhere", 'zipcode':"33333" })
        self.assertTrue(form_Dave.is_valid())

        #Form with wrong state
        form_Lost = clientForm(data = {'full_name':"Lost", 'address_1':"3333 Nowhere St.", 'state':"TT", 'city':"Somewhere", 'zipcode':"33333" })
        self.assertFalse(form_Lost.is_valid())

        #Form with Address 2 but not 1
        form_Confused = clientForm(data = {'full_name':"Confused", 'address_2':"3333 Nowhere St.", 'state':"TT", 'city':"Somewhere", 'zipcode':"33333" })
        self.assertFalse(form_Confused.is_valid())

        #Form with an invalid ZipCode
        form_Zippy = clientForm(data = {'full_name':"Confused", 'address_1':"3333 Nowhere St.", 'state':"TT", 'city':"Somewhere", 'zipcode':"1" })
        self.assertFalse(form_Zippy.is_valid())


    def test_validity_model(self):
        #Valid Client no 2nd address
        dave = Client.objects.get(name="Dave")
        #Valis Client with 2nd address
        betty = Client.objects.get(name="Betty")

        #Check general object intialization
        #address1
        self.assertEqual(dave.stAddress1, "3333 Nowhere st.")
        self.assertEqual(betty.stAddress1, "444 None ave.")
        #address2
        self.assertEqual(dave.stAddress2, "")
        self.assertEqual(betty.stAddress2, "3234 h bl.")
        #state
        self.assertEqual(dave.state, "TX")
        self.assertEqual(betty.state, "AL")
        #city
        self.assertEqual(dave.city, "Somewhere")
        self.assertEqual(betty.city, "u")
        #zip
        self.assertEqual(dave.zip, "33333")
        self.assertEqual(betty.zip, "7777")

        #check labels
        field_label_N_D = dave._meta.get_field('name').verbose_name
        field_label_AO_D = dave._meta.get_field('stAddress1').verbose_name
        field_label_AT_D = dave._meta.get_field('stAddress2').verbose_name
        field_label_S_D = dave._meta.get_field('state').verbose_name
        field_label_C_D= dave._meta.get_field('city').verbose_name
        field_label_Z_D = dave._meta.get_field('zip').verbose_name

        self.assertEqual(field_label_N_D, 'name')
        self.assertEqual(field_label_AO_D, 'stAddress1')
        self.assertEqual(field_label_AT_D, 'stAddress2')
        self.assertEqual(field_label_S_D, 'state')
        self.assertEqual(field_label_C_D, 'city')
        self.assertEqual(field_label_Z_D, 'zip')


    def test_template(self):
        tempresponse = self.client.get('/1/editClient/')
        self.assertEqual(tempresponse.status_code, 200)
        self.assertTemplateUsed(tempresponse, 'ClientForm.html')
        fuelresponse = self.client.get('/1/QuoteHistory/')
        self.assertEqual(fuelresponse.status_code, 200)
        self.assertTemplateUsed(fuelresponse, 'FuelQuoteHist.html')

    def test_completeurl(self):
        compresponse = self.client.get('/1/editClient/complete/')
        self.assertEqual(compresponse.status_code, 200)