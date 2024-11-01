from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User, Apartment, Flat, Lease, Interested
from datetime import date, timedelta

class UserModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'contact_number': '1234567890',
            'contact_email': 'test@gmail.com',
            'password': 'testpassword',
            'user_type': 'User',
            'dob': date(1990, 1, 1),
            'gender': 'M',
            'name': 'Test User'
        }

    def test_create_user(self):
        user = User.objects.create(**self.user_data)
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), self.user_data['username'])

    def test_user_fields(self):
        user = User.objects.create(**self.user_data)
        for field, value in self.user_data.items():
            self.assertEqual(getattr(user, field), value)

    def test_user_type_choices(self):
        user = User.objects.create(**self.user_data)
        self.assertIn(user.user_type, dict(User.USER_TYPE_CHOICES))

    def test_unique_username(self):
        User.objects.create(**self.user_data)
        with self.assertRaises(Exception):
            User.objects.create(**self.user_data)

    def test_email_validation(self):
        self.user_data['contact_email'] = 'invalid_email'
        with self.assertRaises(ValidationError):
            user = User(**self.user_data)
            user.full_clean()

    def test_user_details(self):
        user = User.objects.create(**self.user_data)
        for field, value in self.user_data.items():
            self.assertEqual(getattr(user, field), value)

class ApartmentModelTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create(username='owner', user_type='Owner', contact_email='owner@gmail.com', dob=date(1980, 1, 1))
        self.apartment_data = {
            'address': '123 Test St',
            'facilities': 'Test facilities',
            'owner_id': self.owner,
            'name': 'Test Apartment'
        }

    def test_create_apartment(self):
        apartment = Apartment.objects.create(**self.apartment_data)
        self.assertTrue(isinstance(apartment, Apartment))
        self.assertEqual(apartment.__str__(), self.apartment_data['name'])

    def test_apartment_fields(self):
        apartment = Apartment.objects.create(**self.apartment_data)
        for field, value in self.apartment_data.items():
            self.assertEqual(getattr(apartment, field), value)

    def test_unique_name(self):
        Apartment.objects.create(**self.apartment_data)
        with self.assertRaises(Exception):
            Apartment.objects.create(**self.apartment_data)

    def test_apartment_details(self):
        apartment = Apartment.objects.create(**self.apartment_data)
        for field, value in self.apartment_data.items():
            self.assertEqual(getattr(apartment, field), value)

class FlatModelTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create(username='owner', user_type='Owner', contact_email='owner@gmail.com', dob=date(1980, 1, 1))
        self.apartment = Apartment.objects.create(name='Test Apt', address='123 Test St', owner_id=self.owner)
        self.flat_data = {
            'availability': True,
            'associated_apt_name': self.apartment,
            'rent_per_room': 1000,
            'floor_number': 2,
            'flat_number': 3,
            'ownername': self.owner
        }

    def test_create_flat(self):
        flat = Flat.objects.create(**self.flat_data)
        self.assertTrue(isinstance(flat, Flat))
        self.assertEqual(flat.__str__(), f"{self.apartment.name}_2_3")

    def test_flat_fields(self):
        flat = Flat.objects.create(**self.flat_data)
        for field, value in self.flat_data.items():
            self.assertEqual(getattr(flat, field), value)

    def test_flat_identifier_generation(self):
        flat = Flat.objects.create(**self.flat_data)
        expected_identifier = f"{self.apartment.name}_{self.flat_data['floor_number']}_{self.flat_data['flat_number']}"
        self.assertEqual(flat.flat_identifier, expected_identifier)

    def test_unique_flat_identifier(self):
        Flat.objects.create(**self.flat_data)
        with self.assertRaises(Exception):
            Flat.objects.create(**self.flat_data)

    def test_flat_details(self):
        flat = Flat.objects.create(**self.flat_data)
        for field, value in self.flat_data.items():
            self.assertEqual(getattr(flat, field), value)

class InterestedModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user', contact_email='user@gmail.com', dob=date(1990, 1, 1))
        self.owner = User.objects.create(username='owner', user_type='Owner', contact_email='owner@gmail.com', dob=date(1980, 1, 1))
        self.apartment = Apartment.objects.create(name='Test Apt', address='123 Test St', owner_id=self.owner)
        self.flat = Flat.objects.create(
            associated_apt_name=self.apartment,
            rent_per_room=1000,
            floor_number=2,
            flat_number=3,
            ownername=self.owner
        )
        self.interested_data = {
            'apartment_name': self.apartment,
            'flat_identifier': self.flat,
            'username': self.user
        }

    def test_create_interested(self):
        interested = Interested.objects.create(**self.interested_data)
        self.assertTrue(isinstance(interested, Interested))

    def test_interested_fields(self):
        interested = Interested.objects.create(**self.interested_data)
        for field, value in self.interested_data.items():
            self.assertEqual(getattr(interested, field), value)

class LeaseModelTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create(username='owner', user_type='Owner', contact_email='owner@gmail.com', dob=date(1980, 1, 1))
        self.tenant = User.objects.create(username='tenant', contact_email='tenant@gmail.com', dob=date(1990, 1, 1))
        self.apartment = Apartment.objects.create(name='Test Apt', address='123 Test St', owner_id=self.owner)
        self.flat = Flat.objects.create(
            associated_apt_name=self.apartment,
            rent_per_room=1000,
            floor_number=2,
            flat_number=3,
            ownername=self.owner
        )
        self.lease_data = {
            'lease_start_date': date.today(),
            'lease_end_date': date.today() + timedelta(days=365),
            'flat_identifier': self.flat,
            'tenant_name': self.tenant.username,
            'ownername': self.owner,
            'lease_identifier': f"{self.flat.flat_identifier}_{self.tenant.username}"
        }

    def test_create_lease(self):
        lease = Lease.objects.create(**self.lease_data)
        self.assertTrue(isinstance(lease, Lease))
        self.assertEqual(lease.__str__(), self.lease_data['lease_identifier'])

    def test_lease_fields(self):
        lease = Lease.objects.create(**self.lease_data)
        for field, value in self.lease_data.items():
            self.assertEqual(getattr(lease, field), value)

    def test_unique_lease_identifier(self):
        Lease.objects.create(**self.lease_data)
        with self.assertRaises(Exception):
            Lease.objects.create(**self.lease_data)

    def test_lease_dates(self):
        lease = Lease.objects.create(**self.lease_data)
        self.assertLess(lease.lease_start_date, lease.lease_end_date)

    def test_lease_fields(self):
        lease = Lease.objects.create(**self.lease_data)
        for field, value in self.lease_data.items():
            self.assertEqual(getattr(lease, field), value)
