from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Pen
from django.urls import reverse


class PenTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="penuser",
            email="penuser@email.com",
            password="testpass123",
        )

        cls.pen = Pen.objects.create(
            name="Pen 1",
            owner=cls.user,
            creator="Unknown",
            nib_size="Medium",
            purchase_date="2025-02-01",
            color="Black",
            manufacture_year=2024,
            purchase_location="Vancouver, BC",
            description="Test description",
            favorite=True,
        )

    def test_pen_details(self):
        self.assertEqual(f"{self.pen.name}", "Pen 1")
        self.assertEqual(f"{self.pen.owner.username}", "penuser")
        self.assertEqual(f"{self.pen.creator}", "Unknown")
        self.assertEqual(f"{self.pen.nib_size}", "Medium")
        self.assertEqual(f"{self.pen.purchase_date}", "2025-02-01")
        self.assertEqual(f"{self.pen.color}", "Black")
        self.assertEqual(self.pen.manufacture_year, 2024)
        self.assertEqual(f"{self.pen.purchase_location}", "Vancouver, BC")
        self.assertEqual(f"{self.pen.description}", "Test description")
        self.assertEqual(self.pen.favorite, True)

    def test_pen_list_view_for_logged_in_user(self):
        self.client.login(username="penuser", password="testpass123")
        response = self.client.get(reverse("pen_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your pens")
        self.assertTemplateUsed(response, "pen_list.html")

    def test_pen_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("pen_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/pens/" % (reverse("login")))
        response = self.client.get("%s?next=/pens/" % (reverse("login")))
        self.assertContains(response, "Log In")
