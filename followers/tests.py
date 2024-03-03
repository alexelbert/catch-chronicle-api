from django.contrib.auth.models import User
from django.urls import reverse
from django.db import transaction
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Follower


class FollowListTest(APITestCase):
    """
    Tests for the FollowerList view.
    """

    def setUp(self):
        # Create two test users
        self.user1 = User.objects.create_user(
            username="testuser1",
            password="testpassword"
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            password="testpassword"
        )

        self.client = APIClient()
        self.url = reverse("followers")

    def test_user_can_list_follows(self):
        Follower.objects.create(owner=self.user1, followed=self.user2)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_follow(self):
        self.client.login(username="testuser1", password="testpassword")
        response = self.client.post(self.url, {"followed": self.user2.id})
        count = Follower.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count, 1)

    def test_logged_out_user_cannot_create_follow(self):
        response = self.client.post(self.url, {"followed": self.user2.id})
        count = Follower.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cannot_follow_same_user_twice(self):
        self.client.login(username="testuser1", password="testpassword")
        Follower.objects.create(owner=self.user1, followed=self.user2)
        with transaction.atomic():
            response = self.client.post(self.url, {"followed": self.user2.id})
        count = Follower.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class FollowDetailTest(APITestCase):
    """
    Tests for the FollowerDetail view.
    """

    def setUp(self):
        # Create test users and a follow relationship
        self.user1 = User.objects.create_user(
            username="testuser1",
            password="testpassword"
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            password="testpassword"
        )

        self.follow = Follower.objects.create(
            owner=self.user1,
            followed=self.user2
        )

        self.client = APIClient()
        self.url = reverse("followers_detail", args=[self.follow.id])

    def test_user_can_retrieve_follow(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_delete_own_follow(self):
        self.client.login(username="testuser1", password="testpassword")
        response = self.client.delete(self.url)
        count = Follower.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_another_users_follow(self):
        self.client.login(username="testuser2", password="testpassword")
        response = self.client.delete(self.url)
        count = Follower.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
