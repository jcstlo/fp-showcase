from django.urls import path

from .views import SignUpView, UserUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("settings/", UserUpdateView.as_view(), name="settings"),
]
