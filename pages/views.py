from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model
from fp_showcase.mixins import DemoMixin


class HomePageView(DemoMixin, TemplateView):
    template_name = "home.html"


class ProfileView(DemoMixin, DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "profile_user"
