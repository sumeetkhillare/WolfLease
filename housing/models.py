from django.db import models
import uuid

# Create your models here.
class Owner(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_number = models.CharField(max_length=12)
    contact_email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)


class Apartment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    address = models.CharField(max_length=256)
    facilities = models.CharField(max_length=512)
    owner_id = models.ForeignKey(to=Owner, on_delete=models.DO_NOTHING)