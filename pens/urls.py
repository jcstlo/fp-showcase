from django.urls import path

from .views import AddPenView, PenListView, PenUpdateView, PenDeleteView, PenDetailView

urlpatterns = [
    path("add/", AddPenView.as_view(), name="add_pen"),
    path("edit/<uuid:pk>", PenUpdateView.as_view(), name="update_pen"),
    path("", PenListView.as_view(), name="pen_list"),
    path("delete/<uuid:pk>", PenDeleteView.as_view(), name="delete_pen"),
    path("view/<uuid:pk>", PenDetailView.as_view(), name="pen_detail"),
]
