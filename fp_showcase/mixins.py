from django.conf import settings


class DemoMixin:
    """
    Adds fps_demo to the template context.
    """

    def get_context_data(self, **kwargs):
        fps_demo = settings.FPS_DEMO
        context = super().get_context_data(**kwargs)
        context["fps_demo"] = fps_demo
        return context
