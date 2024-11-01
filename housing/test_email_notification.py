import unittest
from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.conf import settings
from housing.models import User, Lease, Flat, Apartment
from housing.signals import send_mail
from datetime import date
import requests

class SignalsTestCase(TestCase):

    def setUp(self):
        self.owner = User.objects.create(
            username="owner",
            contact_email="owner@gmail.com",
            user_type="Owner",
            dob=date(1990, 1, 1)
        )
        self.tenant = User.objects.create(
            username="tenant",
            contact_email="tenant@gmail.com",
            user_type="User",
            dob=date(1995, 1, 1)
        )
        self.apartment = Apartment.objects.create(
            name="Test Apartment",
            address="123 Test St",
            owner_id=self.owner
        )
        self.flat = Flat.objects.create(
            associated_apt_name=self.apartment,
            floor_number=1,
            flat_number=101,
            rent_per_room=1000,
            ownername=self.owner
        )

    @patch('housing.signals.requests.post')
    def test_send_mail_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = send_mail("test@gmail.com", "Test Subject", "Test Content")
        self.assertEqual(response.status_code, 200)

    @patch('housing.signals.requests.post')
    def test_send_mail_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        response = send_mail("test@gmail.com", "Test Subject", "Test Content")
        self.assertEqual(response.status_code, 400)

    @patch('housing.signals.send_mail')
    def test_send_lease_created_email(self, mock_send_mail):
        lease = Lease.objects.create(
            lease_start_date=date(2023, 1, 1),
            lease_end_date=date(2024, 1, 1),
            flat_identifier=self.flat,
            tenant_name=self.tenant.username,
            ownername=self.owner,
            lease_identifier="TEST_LEASE"
        )
        
        self.assertEqual(mock_send_mail.call_count, 2)

    def test_send_mail_with_invalid_email(self):
        with self.assertRaises(ValueError):
            send_mail("invalid_email", "Test Subject", "Test Content")

    def test_send_mail_with_invalid_email2(self):
        with self.assertRaises(ValueError):
            send_mail("invalid_email@mail.com", "Test Subject", "Test Content")

    def test_send_mail_with_content_and_subject_empty(self):
        with self.assertRaises(ValueError):
            send_mail("invalid_email", "", "")

    @patch('housing.signals.send_mail')
    def test_send_lease_created_email_content(self, mock_send_mail):
        lease = Lease.objects.create(
            lease_start_date=date(2023, 1, 1),
            lease_end_date=date(2024, 1, 1),
            flat_identifier=self.flat,
            tenant_name=self.tenant.username,
            ownername=self.owner,
            lease_identifier="TEST_LEASE"
        )
        
        expected_subject = f"Lease Created between owner: {self.owner}, tenant:{self.tenant}"
        expected_text = f"The lease is created between owner: {self.owner}, tenant:{self.tenant} for {self.flat.flat_identifier}\nDuration - from: {lease.lease_start_date} to {lease.lease_end_date}"
        
        mock_send_mail.assert_any_call(self.owner.contact_email, expected_subject, expected_text)
        mock_send_mail.assert_any_call(self.tenant.contact_email, expected_subject, expected_text)

    @patch('housing.signals.send_mail')
    def test_send_lease_created_email_not_called_on_update(self, mock_send_mail):
        lease = Lease.objects.create(
            lease_start_date=date(2023, 1, 1),
            lease_end_date=date(2024, 1, 1),
            flat_identifier=self.flat,
            tenant_name=self.tenant.username,
            ownername=self.owner,
            lease_identifier="TEST_LEASE"
        )
        
        mock_send_mail.reset_mock()
        
        lease.is_signed = True
        lease.save()
        
        mock_send_mail.assert_not_called()

    @patch('housing.signals.requests.post')
    def test_send_mail_api_call(self, mock_post):
        send_mail("test@gmail.com", "Test Subject", "Test Content")
        
        mock_post.assert_called_once_with(
            f"https://api.mailgun.net/v3/{settings.DOMAIN}/messages",
            auth=("api", settings.API_KEY),
            data={
                "from": settings.FROM,
                "to": ["test@gmail.com"],
                "subject": "Test Subject",
                "text": "Test Content"
            }
        )

    @patch('housing.signals.send_mail')
    def test_send_lease_created_email_exception_handling(self, mock_send_mail):
        
        lease = Lease.objects.create(
            lease_start_date=date(2023, 1, 1),
            lease_end_date=date(2024, 1, 1),
            flat_identifier=self.flat,
            tenant_name=self.tenant.username,
            ownername=self.owner,
            lease_identifier="TEST_LEASE"
        )
        
        # The test passes if no exception is raised

    @patch('housing.signals.send_mail')
    def test_send_lease_created_email_missing_tenant(self, mock_send_mail):
        self.tenant.delete()
        
        with self.assertRaises(User.DoesNotExist):
            Lease.objects.create(
                lease_start_date=date(2023, 1, 1),
                lease_end_date=date(2024, 1, 1),
                flat_identifier=self.flat,
                tenant_name="non_existent_tenant",
                ownername=self.owner,
                lease_identifier="TEST_LEASE"
            )

    def test_send_mail_empty_email(self):
        with self.assertRaises(ValueError):
            send_mail("", "Test Subject", "Test Content")

    def test_send_mail_empty_subject(self):
        with self.assertRaises(ValueError):
            send_mail("test@example.com", "", "Test Content")

    def test_send_mail_empty_content(self):
        with self.assertRaises(ValueError):
            send_mail("test@example.com", "Test Subject", "")

    @patch('housing.signals.requests.post')
    def test_send_mail_network_error(self, mock_post):
        mock_post.side_effect = requests.exceptions.RequestException("Network error")
        
        with self.assertRaises(requests.exceptions.RequestException):
            send_mail("test@gmail.com", "Test Subject", "Test Content")

    @patch('housing.signals.requests.post')
    def test_send_mail_timeout(self, mock_post):
        mock_post.side_effect = requests.exceptions.Timeout("Timeout error")
        
        with self.assertRaises(requests.exceptions.Timeout):
            send_mail("test@gmail.com", "Test Subject", "Test Content")

    def test_send_mail_wrong_mail(self):
        with self.assertRaises(ValueError):
            send_mail("test@test.com", "Test", "Test Content")

    @patch('housing.signals.send_mail')
    def test_send_lease_created_email_long_content(self, mock_send_mail):
        long_text = "a" * 10000
        lease = Lease.objects.create(
            lease_start_date=date(2023, 1, 1),
            lease_end_date=date(2024, 1, 1),
            flat_identifier=self.flat,
            tenant_name=self.tenant.username,
            ownername=self.owner,
            lease_identifier=long_text
        )
        
        mock_send_mail.assert_called()

    @patch('housing.signals.send_mail')
    def test_send_lease_created_email_special_characters(self, mock_send_mail):
        special_chars = "!@#$%^&*()_+{}|:<>?~`-=[]\\;',./'"
        lease = Lease.objects.create(
            lease_start_date=date(2023, 1, 1),
            lease_end_date=date(2024, 1, 1),
            flat_identifier=self.flat,
            tenant_name=self.tenant.username,
            ownername=self.owner,
            lease_identifier=special_chars
        )
        
        mock_send_mail.assert_called()

    @patch('housing.signals.send_mail')
    def test_send_lease_created_email_unicode_characters(self, mock_send_mail):
        unicode_chars = "こんにちは世界"
        lease = Lease.objects.create(
            lease_start_date=date(2023, 1, 1),
            lease_end_date=date(2024, 1, 1),
            flat_identifier=self.flat,
            tenant_name=self.tenant.username,
            ownername=self.owner,
            lease_identifier=unicode_chars
        )
        
        mock_send_mail.assert_called()

if __name__ == '__main__':
    unittest.main()