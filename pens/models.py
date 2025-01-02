import uuid
from django.db import models
from django.conf import settings


class Pen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    creator = models.CharField(max_length=200, blank=True)
    nib_size = models.CharField(max_length=30, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=50, blank=True)
    manufacture_year = models.PositiveSmallIntegerField(null=True, blank=True)
    purchase_location = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    favorite = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
