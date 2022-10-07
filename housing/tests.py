from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from housing.models import Owner

class OwnerTests(APITestCase):
    def test_create_owner(self):
        """
        Ensure we can create a new Owner object.
        """
        url = '/owners/'
        data = {'contact_number': '1234567890', 'contact_email': 'test@testing.com', 'password': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Owner.objects.count(), 1)
        self.assertEqual(Owner.objects.get().contact_email, 'test@testing.com')

    def test_show_owner(self):
        """
        Ensure we can fetch a new Owner object.
        """
        url = '/owners/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Owner.objects.count(), 0)

    def test_update_owner(self):
        """
        Ensure we can update a new Owner object.
        """
        url = '/owners/'
        data = {'contact_number': '1234567890', 'contact_email': 'test@testing.com', 'password': 'test'}
        response = self.client.post(url, data, format='json')
        url = url + str(Owner.objects.get().id) + '/'
        data = {'contact_number': '1234567890', 'contact_email': 'test123@testing.com', 'password': 'test'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Owner.objects.count(), 1)
        self.assertEqual(Owner.objects.get().contact_email, 'test123@testing.com')

    def test_delete_owner(self):
        """
        Ensure we can update a new Owner object.
        """
        url = '/owners/'
        data = {'contact_number': '1234567890', 'contact_email': 'test@testing.com', 'password': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(Owner.objects.count(), 1)
        url = url + str(Owner.objects.get().id) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Owner.objects.count(), 0)
