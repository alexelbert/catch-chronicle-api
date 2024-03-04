from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Notification
from likes.models import Like
from comments.models import Comment
from followers.models import Follower
from catches.models import Catch


def create_notification(**kwargs):
    Notification.objects.create(
        owner=kwargs["owner"],
        sender=kwargs["sender"],
        category=kwargs["category"],
        item_id=kwargs["item_id"],
        title=kwargs["title"],
        content=kwargs["content"],
    )


# Instructions for signals from:
# https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/
@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        data = {
            "owner": instance.catch.owner,
            "sender": instance.owner,
            "category": "like",
            "item_id": instance.catch.id,
            "title": "You have a new like!",
            "content": f"{instance.owner.username} liked your catch "
            f"{instance.catch.title}",
        }

        create_notification(**data)


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        data = {
            "owner": instance.catch.owner,
            "sender": instance.owner,
            "category": "comment",
            "item_id": instance.catch.id,
            "title": "You have a new comment!",
            "content": f"{instance.owner.username} commented on your catch "
            f"{instance.catch.title}",
        }

        create_notification(**data)


@receiver(post_save, sender=Follower)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        data = {
            "owner": instance.followed,
            "sender": instance.owner,
            "category": "follow",
            "item_id": instance.id,
            "title": "You have a new follower!",
            "content": f"{instance.owner.username} is now following you.",
        }

        create_notification(**data)


@receiver(post_save, sender=Catch)
def create_new_sound_notification(sender, instance, created, **kwargs):
    if created:
        recipients = User.objects.filter(following__followed=instance.owner)
        for recipient in recipients:
            data = {
                "owner": recipient,
                "sender": instance.owner,
                "category": "new_sound",
                "item_id": instance.id,
                "title": "You have a new catch!",
                "content": f"{instance.owner.username} uploaded a new catch.",
            }

            create_notification(**data)
