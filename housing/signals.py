# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Lease, User
import requests
from django.conf import settings

def send_mail(mail, subject, text):
    if mail == "" or "@gmail.com" not in mail or subject == "" or text == "":
        raise ValueError()
    api_key = settings.API_KEY
    domain = settings.DOMAIN
    from_address = settings.FROM
    api_key = api_key
    domain = domain
    s = f"https://api.mailgun.net/v3/{domain}/messages"
    return requests.post(s,
        auth=("api", api_key),
        data={
            "from": from_address,
            "to": [mail],
            "subject": subject,
            "text": text
            })

@receiver(post_save, sender=Lease)
def send_lease_created_email(sender, instance, created, **kwargs):
    if created:
        tenant = User.objects.get(username=instance.tenant_name)
        owner = User.objects.get(username=instance.ownername)
        subject = f"Lease Created between owner: {owner}, tenant:{tenant}"
        text = f"The lease is created between owner: {owner}, tenant:{tenant} for {instance.flat_identifier}\nDuration - from: {instance.lease_start_date} to {instance.lease_end_date}"
        response1 = send_mail(owner.contact_email, subject, text)
        response2 = send_mail(tenant.contact_email, subject, text)
        if response1.status_code != 200 or response2 != 200:
            print(f"Request failed: response1 status code = {response1.status_code}, response2 status code = {response2.status_code}")
            