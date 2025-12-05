# from django.test import TestCase
# from .models import Menu, Booking
# from datetime import datetime

# # TestCase class
# class MenuItemTest(TestCase):
#     def test_create_item(self):
#         item = Menu.objects.create(title="IceCream", price=80, inventory=100)
#         self.assertEqual(str(item), "IceCream : 80")
        
#     def test_default_inventory(self):
#         item = Menu.objects.create(title="Cake", price=50, inventory=0)
#         self.assertEqual(item.inventory, 0)


# class BookingTest(TestCase):

#     def test_create_booking(self):
#         booking = Booking.objects.create(
#             name="John Doe",
#             no_of_guest=4,
#             bookingDate=datetime(2023, 6, 24, 18, 0)
#         )
#         expected_str = "John Doe for 4 guests on 2023-06-24 18:00:00"
#         self.assertEqual(str(booking), expected_str)

#     def test_default_number_of_guests(self):
#         booking = Booking.objects.create(
#             name="Jane Doe",
#             bookingDate=datetime(2023, 6, 24, 19, 0),
#             no_of_guest = 6
#         )
#         self.assertEqual(booking.no_of_guest, 6)
