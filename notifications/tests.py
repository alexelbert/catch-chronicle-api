from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Notification


class NotificationTests(APITestCase):
    def setUp(self):
        super().setUp()
        # Setup test users
        self.user1 = User.objects.create_user(
            username='user1',
            password='test1234'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='test1234'
        )

        # Setup notifications for user1
        Notification.objects.create(
            user=self.user1,
            notification_type='Like',
            notification_text='User2 liked your post',
            is_read=False
        )
        Notification.objects.create(
            user=self.user1,
            notification_type='Comment',
            notification_text='User2 commented on your post',
            is_read=False
        )

        # Setup notifications for user2
        Notification.objects.create(
            user=self.user2,
            notification_type='Follow',
            notification_text='User1 followed you',
            is_read=False
        )

        self.client = APIClient()

        print(f"\n{self.id()}")

    def test_list_notifications(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('notifications')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['count'], 2)

        self.assertEqual(len(response.data['results']), 2)

    def test_notification_detail_view(self):
        self.client.force_authenticate(user=self.user1)
        notification = Notification.objects.filter(user=self.user1).first()
        url = reverse('notification_detail', kwargs={'pk': notification.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['notification_text'],
            notification.notification_text
        )

    def test_unauthorized_access(self):
        # Attempt to access user1's notification as user2
        self.client.force_authenticate(user=self.user2)
        notification = Notification.objects.filter(user=self.user1).first()
        url = reverse('notification_detail', kwargs={'pk': notification.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_mark_notification_as_read(self):
        # Mark a notification as read
        self.client.force_authenticate(user=self.user1)
