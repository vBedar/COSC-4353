from django.test import TestCase
from FuelSite.models import User, fuelQuote, Client
from django.utils import timezone

import datetime
import decimal

class pricingTest(TestCase):

    def setUp(self):
        #User Models to relate to
        u1 = User.objects.create(username="user1", password="1234")
        u2 = User.objects.create(username="user2", password="1234")
        u3 = User.objects.create(username="user3", password="1234")
        u4 = User.objects.create(username="user4", password="1234")
        #Fuel Quote Models
        #in-state has history
        #less than 1000 gallons
        fuelQuote.objects.create(user=u1, gallonsRequested = 200, deliveryDate = "2023-08-29", deliveryAddress = "3333 TX")
        #over 1000 gallons
        fuelQuote.objects.create(user=u1, gallonsRequested=10000, deliveryDate = "2022-09-22", deliveryAddress = "3333 TX")
        #out-of-state under 1000
        fuelQuote.objects.create(user=u1, gallonsRequested=200, deliveryDate = "2024-06-21", deliveryAddress = "2222 CO")
        #out-of-state over 1000
        fuelQuote.objects.create(user=u1, gallonsRequested=10000, deliveryDate="2023-01-02", deliveryAddress = "2222 CO")
        #No history in-state under 1000
        fuelQuote.objects.create(user=u2, gallonsRequested=100, deliveryDate="2025-03-13", deliveryAddress = "4444 TX")
        #No history out-of-state under 1000
        fuelQuote.objects.create(user=u3, gallonsRequested=100, deliveryDate="2023-04-06", deliveryAddress = "5555 LA")
        #No history out-of-state over 1000
        fuelQuote.objects.create(user=u4, gallonsRequested=2000, deliveryDate="2022-11-25", deliveryAddress = "5555 LA")

    def test_price_module(self):
        u1p1 = fuelQuote.objects.get(id=1)
        u1p2 = fuelQuote.objects.get(id=2)
        u1p3 = fuelQuote.objects.get(id=3)
        u1p4 = fuelQuote.objects.get(id=4)
        u2p1 = fuelQuote.objects.get(id=5)
        u3p1 = fuelQuote.objects.get(id=6)
        u4p1 = fuelQuote.objects.get(id=7)

        u1p1.get_total_price()
        u1p2.get_total_price()
        u1p3.get_total_price()
        u1p4.get_total_price()
        u2p1.get_total_price()
        u3p1.get_total_price()
        u4p1.get_total_price()

        self.assertEqual()
