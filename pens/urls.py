from django.urls import path

from .views import AddPenView

urlpatterns = [
    path("add", AddPenView.as_view(), name="add_pen"),
]
