from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Pen, PenImage


class DateInput(forms.DateInput):
    input_type = "date"


class PenForm(ModelForm):
    class Meta:
        model = Pen
        fields = (
            "name",
            "description",
            "nib_size",
            "creator",
            "color",
            "manufacture_year",
            "purchase_location",
            "purchase_date",
            "favorite",
        )
        widgets = {
            "purchase_date": DateInput(),
        }
        labels = {
            "creator": _("Brand/company/creator"),
        }


class PenImageForm(ModelForm):
    class Meta:
        model = PenImage
        fields = ("image",)

    # use clean_image() with form_valid() instead of blank=False in the PenImage model,
    # to allow users to create pens without requiring an image to be uploaded.
    # If blank=False, the Django form will show the image form as 'required', which
    # is not the intention
    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            raise forms.ValidationError("An image is required.")
        return image
