from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Comment
from catches.models import Catch


class CommentListTest(APITestCase):
    """Tests for the CommentList view."""

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()
        self.url = reverse("comments")
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
        self.data = {
            "catchId": self.catch.id,
            "content": "testcontent",
        }

        # Print test id
        print(f"\n{self.id()}")

    def test_user_can_list_comments(self):
        Comment.objects.create(owner=self.user, catchId=self.catch)
        response = self.client.get(self.url)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_can_create_comment(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_comment(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(Comment.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailTest(APITestCase):
    """Tests for the CommentDetail view."""

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
        self.comment = Comment.objects.create(
            owner=self.user1, catchId=self.catch
        )
        self.url = reverse("comments_detail", args=[self.comment.id])

        self.data = {
            "owner": self.user1.id,
            "catchId": self.catch.id,
            "content": "testcontent",
        }
        self.updated_data = {
            "catchId": self.catch.id,
            "content": "updatedcontent",
        }

        print(f"\n{self.id()}")

    def test_user_can_retrieve_comment(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_update_own_comment(self):
        self.client.force_login(self.user1)
        response = self.client.put(self.url, self.updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_delete_own_comment(self):
        self.client.force_login(self.user1)
        response = self.client.delete(self.url)
        count = Comment.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_another_users_comment(self):
        self.client.force_login(self.user2)
        response = self.client.delete(self.url)
        count = Comment.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
