from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, blank=False)
    profile_description = models.TextField(_("profile description"), blank=True)
    slug = models.SlugField(_("slug"), unique=True, blank=False, default="slug")
    # profile_picture = models.ImageField(_("profile picture"), )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
