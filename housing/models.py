from ssl import OP_ENABLE_MIDDLEBOX_COMPAT
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

class Lease(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()

class Flat(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    availability = models.BooleanField(default=False)
    associated_apt_id = models.ForeignKey(to=Apartment, on_delete=models.DO_NOTHING)
    lease_id = models.ForeignKey(to=Lease, on_delete=models.DO_NOTHING)
    rent_per_room = models.IntegerField()
    floor_number = models.IntegerField()