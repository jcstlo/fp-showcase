from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.http import Http404
from django.contrib.auth.views import LoginView
from fp_showcase.mixins import DemoMixin


class SignUpView(DemoMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomLoginView(DemoMixin, LoginView):
    pass


class UserUpdateView(DemoMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    fields = [
        "profile_picture",
    ]
    template_name = "profile_settings.html"
    success_url = reverse_lazy("home")

    # override SingleObjectMixin's get_object() to return the current user object instead,
    # so user ID doesn't need to be exposed in URL
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.request.user.pk
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError(
                "Error with retrieving user for profile settings page."
            )

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user
