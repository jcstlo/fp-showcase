from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView
from django.contrib.auth import get_user_model


class HomepageTests(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Home")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This should not be on the page")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def test_homepage_view_for_logged_in_user(self):
        new_user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpass123",
        )
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Hello,")
        self.assertContains(response, "testuser")
        self.assertNotContains(response, "Show your collection of fountain pens")

    def test_homepage_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Show your collection of fountain pens")
        self.assertNotContains(response, "Hello,")
