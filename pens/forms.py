from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Pen


class DateInput(forms.DateInput):
    input_type = "date"


class PenForm(ModelForm):
    class Meta:
        model = Pen
        fields = (
            "name",
            "creator",
            "description",
            "nib_size",
            "color",
            "manufacture_year",
            "purchase_location",
            "purchase_date",
            "favorite",
            "main_image",
        )
        widgets = {
            "purchase_date": DateInput(),
        }
        labels = {
            "name": _("Name/model"),
            "creator": _("Brand/company/creator"),
        }
