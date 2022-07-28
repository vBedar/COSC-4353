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
        u5 = User.objects.create(username="user5", password="1234")
        #Fuel Quote Models
        #in-state has history
        #less than 1000 gallons
        fuelQuote.objects.create(user=u1, gallonsRequested = 200, deliveryDate = "2023-08-29", deliveryAddress = "3333 TX", suggestedPrice = 0, totalAmountDue = 0)
        #over 1000 gallons
        fuelQuote.objects.create(user=u1, gallonsRequested=10000, deliveryDate = "2022-09-22", deliveryAddress = "3333 TX", suggestedPrice = 0, totalAmountDue = 0)
        #out-of-state under 1000
        fuelQuote.objects.create(user=u1, gallonsRequested=200, deliveryDate = "2024-06-21", deliveryAddress = "2222 CO", suggestedPrice = 0, totalAmountDue = 0)
        #out-of-state over 1000
        fuelQuote.objects.create(user=u1, gallonsRequested=10000, deliveryDate="2023-01-02", deliveryAddress = "2222 CO", suggestedPrice = 0, totalAmountDue = 0)
        #No history in-state under 1000
        fuelQuote.objects.create(user=u2, gallonsRequested=100, deliveryDate="2025-03-13", deliveryAddress = "4444 TX", suggestedPrice = 0, totalAmountDue = 0)
        #No history out-of-state under 1000
        fuelQuote.objects.create(user=u3, gallonsRequested=100, deliveryDate="2023-04-06", deliveryAddress = "5555 LA", suggestedPrice = 0, totalAmountDue = 0)
        #No history out-of-state over 1000
        fuelQuote.objects.create(user=u4, gallonsRequested=2000, deliveryDate="2022-11-25", deliveryAddress = "5555 LA", suggestedPrice = 0, totalAmountDue = 0)
        #No history in-state over 1000
        fuelQuote.objects.create(user=u5, gallonsRequested=2000, deliveryDate="2025-12-25", deliveryAddress = "4444 TX", suggestedPrice = 0, totalAmountDue = 0)

    def test_price_module(self):
        u1p1 = fuelQuote.objects.get(id=1)
        u1p2 = fuelQuote.objects.get(id=2)
        u1p3 = fuelQuote.objects.get(id=3)
        u1p4 = fuelQuote.objects.get(id=4)
        u2p1 = fuelQuote.objects.get(id=5)
        u3p1 = fuelQuote.objects.get(id=6)
        u4p1 = fuelQuote.objects.get(id=7)
        u5p1 = fuelQuote.objects.get(id=8)

        u1p1.get_total_price()
        u1p2.get_total_price()
        u1p3.get_total_price()
        u1p4.get_total_price()
        u2p1.get_total_price()
        u3p1.get_total_price()
        u4p1.get_total_price()
        u5p1.get_total_price()
        
        #u1p1 sp = 1.5 + (1.5*(.02-.01+.03+.1)) = 1.71 * 200 = 342
        self.assertEqual(u1p1.suggestedPrice, 1.71)
        self.assertEqual(u1p1.totalAmountDue, 342.00)
        #u1p2 sp = 1.5 + (1.5*(.02-.01+.02+.1)) = 1.695 * 10000 = 16950
        self.assertEqual(u1p2.suggestedPrice, 1.695)
        self.assertEqual(u1p2.totalAmountDue, 16950.00)
        #u1p3 sp = 1.5 + (1.5*(.04-.01+.03+.1)) = 1.74 * 200 = 348
        self.assertEqual(u1p3.suggestedPrice, 1.74)
        self.assertEqual(u1p3.totalAmountDue, 348.00)
        #u1p4 sp = 1.5 + (1.5*(.04-.01+.02+.1)) = 1.725 * 10000 = 17250
        self.assertEqual(u1p4.suggestedPrice, 1.725)
        self.assertEqual(u1p4.totalAmountDue, 17250.00)
        #u2p1 sp = 1.5 + (1.5*(.02-0+.03+.1)) = 1.725 * 100 = 172.50
        self.assertEqual(u2p1.suggestedPrice, 1.725)
        self.assertEqual(u2p1.totalAmountDue, 172.50)
        #u3p1 sp = 1.5 + (1.5*(.04-0+.03+.1)) = 1.755 * 100 = 175.50
        self.assertEqual(u3p1.suggestedPrice, 1.755)
        self.assertEqual(u3p1.totalAmountDue, 175.50)
        #u4p1 sp = 1.5 + (1.5*(.04-0+.02+.1)) = 1.74 * 2000 = 3480
        self.assertEqual(u4p1.suggestedPrice, 1.74)
        self.assertEqual(u4p1.totalAmountDue, 3480.00)
        #u5p1 sp = 1.5 + (1.5*(.02-0+.02+.1)) = 1.71 * 2000 = 3420
        self.assertEqual(u5p1.suggestedPrice, 1.71)
        self.assertEqual(u5p1.totalAmountDue, 3420.00)
