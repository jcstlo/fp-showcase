from django.contrib import admin

from .models import Pen, PenImage


class PenAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )


admin.site.register(Pen, PenAdmin)
admin.site.register(PenImage)
