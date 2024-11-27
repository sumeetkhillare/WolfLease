"""
    This is a file to add test cases for different models.
"""

from urllib import response
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from housing.models import *
import json



class OwnerTests(APITestCase):
    """
        This is Owner test class.
    """
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
        # Creating objects for this testcase
        Owner.objects.create(contact_number = '11111', contact_email = 'test111@testing.com', password='test123')
        Owner.objects.create(contact_number = '22222', contact_email = 'test222@testing.com', password='test123')
        Owner.objects.create(contact_number = '33333', contact_email = 'test333@testing.com', password='test123')
        url = '/owners'
        url = url + '?search=test222@testing.com'
        response = self.client.get(url)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['contact_number'], '22222')


class InterestedTests(APITestCase, TestCase):
    """
        This is Interested test class.
    """

    @classmethod
    def setUpTestData(cls):
        """
            This is setUp class method to populate the database
        """
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

    """
        This is Flat test class.
    """

    @classmethod
    def setUpTestData(cls):
        """
            This is setUp class method to populate the database
        """
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

    def test_search_flat(self):
        """
            Ensure that we can search a flat with given search paramaters
        """
        Flat.objects.create(availability = 'True', associated_apt_id =  Apartment.objects.get(), lease_id = Lease.objects.get(), rent_per_room = 500, floor_number = 2)
        url = '/flats'
        url = url + '?search=500'
        response = self.client.get(url)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['floor_number'], 2)


class ApartmentTests(APITestCase, TestCase):
    """
        This is Apartment test class.
    """
    @classmethod
    def setUpTestData(cls):
        """
            This is setUp class method to populate the database
        """
        cls.Owner = Owner.objects.create(contact_number='1234567890', contact_email='test@testing.com', password='test')
        cls.Lease = Lease.objects.create(lease_start_date='2022-10-05', lease_end_date='2026-10-04')
        cls.Apartment = Apartment.objects.create(owner_id=Owner.objects.get(), address="Stovall Dr")
        cls.Flat = Flat.objects.create(availability='False', associated_apt_id=Apartment.objects.get(), lease_id=Lease.objects.get(), floor_number=3, rent_per_room=450)
        cls.User = User.objects.create(flat_id = Flat.objects.get(), contact_number='7876756487', dob='2000-10-07')
        cls.Intested = Interested.objects.create(user_id = User.objects.get(), flat_id = Flat.objects.get(), apartment_id = Apartment.objects.get())

    def test_create_apartment(self):
        """
        Ensure that we can create a new Apartment Object
        """

        url = '/apartments'
        data = {'address': '1130 Clarion Heights Ln, Crab Orchard Drive, Raleigh NC 27606', 'facilities' : 'Washer, Dryer, Oven, Swimming Pool, Club House, Gym', 'owner_id' : str(Owner.objects.get().id)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Apartment.objects.count(), 2) #this is because we already created an object in the setup function and other one is right in this function
        self.assertEqual('1130 Clarion Heights Ln, Crab Orchard Drive, Raleigh NC 27606', str(Apartment.objects.filter(facilities = 'Washer, Dryer, Oven, Swimming Pool, Club House, Gym').get().address))

    def test_show_apartment(self):
        """
        Ensure that we are retrieve an apartment object
        """

        url = '/apartments'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Apartment.objects.count(), 1)


    def test_update_apartment(self):
        """
        Ensure we can update the Apartment info
        """
        url = '/apartments'
        url = url + '/' + str(Apartment.objects.get().id)
        data = {'address': '1130 Clarion Heights Ln, Crab Orchard Drive, Raleigh NC 27606'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Apartment.objects.count(), 1)
        self.assertEqual(Apartment.objects.get().address, '1130 Clarion Heights Ln, Crab Orchard Drive, Raleigh NC 27606')

    
    def test_delete_apartment(self):
        """
        Ensure we can delete an Apartment Object
        """

        url = '/apartments'
        url = url + '/' + str(Apartment.objects.get().id)
        # data = {}
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Apartment.objects.count(), 0)



    def test_search_apartment(self):
        """
        Ensure that we can search Apartments with the given search parameters
        """
        Apartment.objects.create(address= 'ClarionHeights', facilities = 'Washer, Dryer, Oven, Swimming Pool, Club House, Gym', owner_id = Owner.objects.get())

        url = '/apartments'
        # need to test this out
        url = url + '?search=ClarionHeights'
        response = self.client.get(url)
        print('Content: '+str(response.content))
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['facilities'], 'Washer, Dryer, Oven, Swimming Pool, Club House, Gym')


class UserTests(APITestCase, TestCase):
    """
        This is User test class.
    """
    @classmethod
    def setUpTestData(cls):
        """
        This is setUp class method to populate the database
        """     
        cls.Owner = Owner.objects.create(contact_number='1234567890', contact_email='test@testing.com', password='test')

        cls.Apartment = Apartment.objects.create(owner_id=Owner.objects.get(), address="Stovall Dr")
        cls.Lease = Lease.objects.create(lease_start_date='2022-10-05', lease_end_date='2026-10-04')
        cls.Flat = Flat.objects.create(availability='True', associated_apt_id=Apartment.objects.get(), lease_id=Lease.objects.get(), floor_number=3, rent_per_room=450)
        cls.User = User.objects.create(flat_id = Flat.objects.get(), contact_number= '7876756487', contact_email= 'rohan@gmail.com',  dob = '2000-10-07')

    def test_create_user(self):
        """
        Ensure that we can create a user
        """

        url = '/users'
        data = {'flat_id' : str(Flat.objects.get().id), 'contact_number': '8454210259', 'contact_email': 'ameya@gmail.com', 'password' : 'password' ,'dob' : '2000-10-10'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2) 

    
    def test_show_user(self):
        """
        Ensure that we are able to retrieve the user details
        """
        url = '/users'
        

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)

    def test_update_user(self):
        """
        Ensure that the user is being updated correctly
        """
        # Creating a User record first
        url = '/users'
        
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Now updating the data with updated phone number
        url = url + '/' + str(User.objects.get().id)
        data = {'flat_id' : Flat.objects.get().id, 'contact_number': '9548751029', 'contact_email': 'rohan@gmail.com',  'dob' : '2000-10-07'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().contact_number, '9548751029')

    def test_delete_user(self):
        """
        Ensure that the user can be deleted
        """
        # Creating the user first 
        url = '/users'


        # Deleting the user
        url = url + '/' + str(User.objects.get().id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)



    def test_search_user(self):
        """
        Ensure that a user can be searched
        """
        User.objects.create(flat_id = Flat.objects.get(), contact_number= '7876756487', contact_email= 'kunal@gmail.com',  dob = '2000-10-07')
        User.objects.create(flat_id = Flat.objects.get(), contact_number= '8454210289', contact_email= 'om@gmail.com',  dob = '2000-05-17')
        User.objects.create(flat_id = Flat.objects.get(), contact_number= '5165151651', contact_email= 'subodh@gmail.com',  dob = '2000-12-06')

        url = '/users'
        url = url + '?search=subodh@gmail.com'
        response = self.client.get(url)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['contact_number'], '5165151651')
        
class LeaseTests(APITestCase, TestCase):

    """
        This is Lease test class.
    """

    def test_create_lease(self):
        """
        Ensure we can create a new Lease object.
        """
        url = '/lease'
        data = {"lease_start_date": "2022-10-05", "lease_end_date": '2026-10-04'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lease.objects.count(), 1)

    def test_show_lease(self):
        """
        Ensure we can fetch a Lease object.
        """
        url = '/lease'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lease.objects.count(), 0)

    def test_update_lease(self):
        """
        Ensure we can update a lease object.
        """
        url = '/lease'
        Lease.objects.create(lease_start_date='2022-10-05', lease_end_date='2026-10-04')
        url = url +'/'+ str(Lease.objects.get().id) 
        data = {"lease_start_date": '2022-12-05'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lease.objects.count(), 1)

    def test_delete_lease(self):
        """
        Ensure we can delete a lease object.
        """
        url = '/lease'
        Lease.objects.create(lease_start_date='2022-10-05', lease_end_date='2026-10-04')
        url = url + '/' + str(Lease.objects.get().id)
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lease.objects.count(), 0)

