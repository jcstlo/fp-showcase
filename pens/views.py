from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Pen
from .forms import PenForm, PenImageForm


class AddPenView(LoginRequiredMixin, CreateView):
    template_name = "add_pen.html"
    form_class = PenForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        pen_image_form = context["pen_image_form"]
        # create a new Pen object
        self.object = form.save()

        # check if an image was added. If so, then create
        # a new PenImage object as well
        if pen_image_form.is_valid():
            pen_image = pen_image_form.save(commit=False)
            pen_image.pen = self.object
            pen_image.save()

        return redirect(self.get_success_url())

    # Include the PenImageForm in the context, to let users
    # add an image when creating a new pen
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["pen_image_form"] = PenImageForm(
                self.request.POST, self.request.FILES
            )
        else:
            context["pen_image_form"] = PenImageForm()

        return context


class PenListView(LoginRequiredMixin, ListView):
    template_name = "pen_list.html"

    def get_queryset(self):
        return Pen.objects.filter(owner=self.request.user)


class PenDetailView(LoginRequiredMixin, DetailView):
    model = Pen
    context_object_name = "pen"


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
