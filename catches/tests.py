from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Catch
from django.core.files.uploadedfile import SimpleUploadedFile


class CatchListViewTests(APITestCase):
    """
    Tests for CatchList view.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        self.client = APIClient()
        self.url = reverse("catch")
        self.data = {
            "caption": "Test caption",
            "species": "Test species",
            "method": "flyrod",
            "weight": 1.5,
            "length": 30.0,
            "location": "Test location",
            "latitude": 0.0,
            "longitude": 0.0,
            "time": "12:00:00",
            "weather": "sunny",
            "lure": "Test lure",
        }

        print(f"\n{self.id()}")

    def test_user_can_list_catches(self):
        Catch.objects.create(
            owner=self.user,
            caption=self.data["caption"],
            species=self.data["species"],
            method=self.data["method"],
            weight=self.data["weight"],
            length=self.data["length"],
            location=self.data["location"],
            latitude=self.data["latitude"],
            longitude=self.data["longitude"],
            time=self.data["time"],
            weather=self.data["weather"],
            lure=self.data["lure"],
        )
        response = self.client.get(self.url)
        count = Catch.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, 200)


class CatchDetailViewTests(APITestCase):
    """
    Tests for CatchDetail view
    """

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="testuser1",
            password="testpassword",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            password="testpassword",
        )
        self.catch = Catch.objects.create(
            owner=self.user1,
            caption="Test caption",
            species="Test species",
            method="flyrod",
            weight=1.5,
            length=30.0,
            location="Test location",
            latitude=0.0,
            longitude=0.0,
            time="12:00:00",
            weather="sunny",
            lure="Test lure",
        )
        self.data = {
            "caption": "Changed caption",
            "species": "Changed species",
            "method": "spinning",
            "weight": 2.0,
            "length": 35.0,
            "location": "Changed location",
            "latitude": 1.0,
            "longitude": 1.0,
            "time": "13:00:00",
            "weather": "cloudy",
            "lure": "Changed lure",
        }

        self.url = reverse("catch_detail", args=[self.catch.id])

        self.client = APIClient()

        print(str(f"\n{self.id()}"))

    def test_get_valid_catch(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["caption"], self.catch.caption)

    def test_get_invalid_catch(self):
        url = reverse("catch_detail", args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authenticated_user_can_update_owned_catch(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["caption"], self.data["caption"])

    def test_user_cannot_update_another_users_catch(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.put(self.url, self.data)
        catch = Catch.objects.get(id=self.catch.id)
        self.assertNotEqual(catch.caption, self.data["caption"])
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_owned_catch(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_unowned_catch(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
