from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Pen


class AddPenView(LoginRequiredMixin, CreateView):
    model = Pen
    template_name = "add_pen.html"
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
    success_url = reverse_lazy("add_pen")  # TODO: change to profile or home page

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
