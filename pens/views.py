from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class PenUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pen
    form_class = PenForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("pen_list")

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class PenDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pen
    success_url = reverse_lazy("pen_list")

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
