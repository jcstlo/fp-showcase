from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from ulid import ULID


def create_ulid_filename(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<ULID>.<filename_ext>
    filename_ext = filename.split(".")[-1]
    ulid = str(ULID())
    ulid_filename = f"{ulid}.{filename_ext}"
    print(f"ulid_filename = {ulid_filename}")
    return ulid_filename


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, blank=False)
    profile_description = models.TextField(_("profile description"), blank=True)
    slug = models.SlugField(_("slug"), unique=True, blank=False, default="slug")
    profile_picture = models.ImageField(
        _("profile picture"),
        upload_to=create_ulid_filename,
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
