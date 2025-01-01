from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Pen
from .forms import PenForm


class AddPenView(LoginRequiredMixin, CreateView):
    template_name = "add_pen.html"
    form_class = PenForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PenListView(LoginRequiredMixin, ListView):
    template_name = "pen_list.html"

    def get_queryset(self):
        return Pen.objects.filter(owner=self.request.user)
