from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import PenForm


class AddPenView(LoginRequiredMixin, CreateView):
    template_name = "add_pen.html"
    form_class = PenForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
