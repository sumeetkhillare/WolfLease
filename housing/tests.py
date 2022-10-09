from urllib import response
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from housing.models import *

class OwnerTests(APITestCase):
    def test_create_owner(self):
        """
        Ensure we can create a new Owner object.
        """
        url = '/owners'
        data = {'contact_number': '1234567890', 'contact_email': 'test@testing.com', 'password': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Owner.objects.count(), 1)
        self.assertEqual(Owner.objects.get().contact_email, 'test@testing.com')

    def test_show_owner(self):
        """
        Ensure we can fetch a new Owner object.
        """
        url = '/owners'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Owner.objects.count(), 0)

    def test_update_owner(self):
        """
        Ensure we can update a new Owner object.
        """
        url = '/owners'
        data = {'contact_number': '1234567890', 'contact_email': 'test@testing.com', 'password': 'test'}
        response = self.client.post(url, data, format='json')
        url = url + '/' + str(Owner.objects.get().id)
        data = {'contact_number': '1234567890', 'contact_email': 'test123@testing.com', 'password': 'test'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Owner.objects.count(), 1)
        self.assertEqual(Owner.objects.get().contact_email, 'test123@testing.com')

    def test_delete_owner(self):
        """
        Ensure we can update a new Owner object.
        """
        url = '/owners'
        data = {'contact_number': '1234567890', 'contact_email': 'test@testing.com', 'password': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(Owner.objects.count(), 1)
        url = url + '/' + str(Owner.objects.get().id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Owner.objects.count(), 0)

    def test_search_owner(self):
        """
        Ensure that we can search an Owner object
        """
        url = '/owners' + '?search=test222@gmail.com'
        response = self.client.get(url)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['contact_number'], '22222')


class InterestedTests(APITestCase, TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Owner = Owner.objects.create(contact_number='1234567890', contact_email='test@testing.com', password='test')
        cls.Lease = Lease.objects.create(lease_start_date='2022-10-05', lease_end_date='2026-10-04')
        cls.Apartment = Apartment.objects.create(owner_id=Owner.objects.get(), address="Stovall Dr")
        cls.Flat = Flat.objects.create(availability='True', associated_apt_id=Apartment.objects.get(), lease_id=Lease.objects.get(), floor_number=3, rent_per_room=450)
        cls.User = User.objects.create(flat_id = Flat.objects.get(), contact_number='7876756487', dob='2000-10-07')
        cls.Intested = Interested.objects.create(user_id = User.objects.get(), flat_id = Flat.objects.get(), apartment_id = Apartment.objects.get())
        cls.otherFlat = Flat.objects.create(availability='True', associated_apt_id=Apartment.objects.get(), lease_id=Lease.objects.get(), floor_number=2, rent_per_room=780)

    def test_create_interested(self):
        """
        Ensure we can create a new interested object.
        """
        url = '/interests'
        data = {'user_id': str(User.objects.get().id), 'flat_id': str(Flat.objects.first().id), 'apartment_id': str(Apartment.objects.get().id)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Interested.objects.count(), 2)
        self.assertEquals(str(User.objects.get()), str(Interested.objects.last().user_id))

    def test_show_interested(self):
        """
        Ensure we can fetch a new interested object.
        """
        url = '/interests'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Interested.objects.count(), 1)

    def test_update_interested(self):
        """
        Ensure we can update a interested object.
        """
        url = '/interests'
        url = url +'/'+ '1'
        data = {'flat_id':str(Flat.objects.last().id)}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Interested.objects.count(), 1)
        self.assertEqual(str(Interested.objects.get().flat_id), str(Flat.objects.last()))

    def test_delete_interested(self):
        """
        Ensure we can delete a new interested object.
        """
        url = '/interests'
        url = url + '/' +'1'
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Interested.objects.count(), 0)

class FlatTests(APITestCase, TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Owner = Owner.objects.create(contact_number='1234567890', contact_email='test@testing.com', password='test')
        cls.Lease = Lease.objects.create(lease_start_date='2022-10-05', lease_end_date='2026-10-04')
        cls.Apartment = Apartment.objects.create(owner_id=Owner.objects.get(), address="Stovall Dr")
        cls.Flat = Flat.objects.create(availability='False', associated_apt_id=Apartment.objects.get(), lease_id=Lease.objects.get(), floor_number=3, rent_per_room=450)
        cls.User = User.objects.create(flat_id = Flat.objects.get(), contact_number='7876756487', dob='2000-10-07')
        cls.Intested = Interested.objects.create(user_id = User.objects.get(), flat_id = Flat.objects.get(), apartment_id = Apartment.objects.get())

    def test_create_flat(self):
        """
        Ensure we can create a new Flat object.
        """
        url = '/flats'
        data = {'availability': 'True', 'associated_apt_id': str(Apartment.objects.get().id), 'lease_id': str(Lease.objects.get().id),'floor_number':'1', 'rent_per_room':'540'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Flat.objects.count(), 2)
        self.assertEquals('True', str(Flat.objects.filter(availability='True').get().availability))

    def test_show_flat(self):
        """
        Ensure we can fetch a flat object.
        """
        url = '/flats'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Interested.objects.count(), 1)

    def test_update_interested(self):
        """
        Ensure we can update a flat object.
        """
        url = '/flats'
        url = url +'/'+ str(Flat.objects.get().id) 
        data = {'availability':'False'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Flat.objects.count(), 1)
        self.assertEqual(str(Flat.objects.get().availability), 'False')

    def test_delete_flat(self):
        """
        Ensure we can delete a flat object.
        """
        url = '/flats'
        url = url + '/' + str(Flat.objects.get().id)
        data = {}
        # User.objects.get().flat_id = None
        response = self.client.delete(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Flat.objects.count(), 0)
