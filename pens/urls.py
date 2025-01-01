from django.urls import path

from .views import AddPenView, PenListView

urlpatterns = [
    path("add/", AddPenView.as_view(), name="add_pen"),
    path("", PenListView.as_view(), name="pen_list"),
]
