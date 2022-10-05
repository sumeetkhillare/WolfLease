
from django.test import SimpleTestCase
from housing import models
# Create your tests here.
class FlatTest(SimpleTestCase):
    def testStringRep(self):
        flat = models.Flat(rent_per_room=1800)
        self.assertEqual(None == flat, False)