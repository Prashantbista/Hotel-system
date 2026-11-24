from django.test import TestCase
from Hotel.models import Client

from django.urls import reverse


class ClientModelTest(TestCase):
    def setUp(self):
        self.hotel_client = Client.objects.create(
            name="Tom",
            email="Tom@gmail.com",
            phone_number=9857665656,
            table=6,
        )

    def test_client_is_created(self):
        self.assertEqual(Client.objects.count(), 1)

    def test_client_name(self):
        self.assertEqual(self.hotel_client.name, "Tom")



class ClientPageTest(TestCase):
    def test_client_list_page(self):
        response=self.client.get(reverse("client"))

        self.assertEqual(response.status_code, 200)
