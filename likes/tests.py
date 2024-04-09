from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Like
from catches.models import Catch


class LikeListTest(APITestCase):
    """
    Tests for the LikeList view.
    """

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()
        self.url = reverse("likes")
        self.catch = Catch.objects.create(
            owner=self.user,
            caption="testcaption",
            species="Test Species",
            method="flyrod",
            weight=1.5,
            length=30.0,
            location="Test Location",
            time="12:00:00",
            weather="sunny",
            lure="Test Lure"
        )

        print(f"\n{self.id()}")

    def test_user_can_list_likes(self):
        Like.objects.create(owner=self.user, catch=self.catch)
        response = self.client.get(self.url)
        count = Like.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_like_catch(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, {"catch": self.catch.id})
        count = Like.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_like_catch(self):
        response = self.client.post(self.url, {"catch": self.catch.id})
        count = Like.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailTest(APITestCase):
    """
    Tests for the LikeDetail view.
    """

    def setUp(self):
        super().setUp()
        self.user1 = User.objects.create_user(
            username="testuser1", password="testpassword"
        )
        self.user2 = User.objects.create_user(
            username="testuser2", password="testpassword"
        )
        self.client = APIClient()
        self.catch = Catch.objects.create(
            owner=self.user1,
            caption="testcaption",
            species="Test Species",
            method="flyrod",
            weight=1.5,
            length=30.0,
            location="Test Location",
            time="12:00:00",
            weather="sunny",
            lure="Test Lure"
        )
        self.like = Like.objects.create(owner=self.user1, catch=self.catch)
        self.url = reverse("like_detail", args=[self.like.id])

        print(f"\n{self.id()}")

    def test_user_can_unlike_catch(self):
        self.client.force_login(self.user1)
        response = self.client.delete(self.url)
        count = Like.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_another_users_like(self):
        self.client.force_login(self.user2)
        response = self.client.delete(self.url)
        count = Like.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
