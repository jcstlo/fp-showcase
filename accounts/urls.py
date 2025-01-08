from django.urls import path

from .views import SignUpView, UserUpdateView, CustomLoginView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("settings/", UserUpdateView.as_view(), name="settings"),
]
