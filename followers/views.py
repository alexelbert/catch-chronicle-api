from rest_framework import generics, permissions
from catch_chronicle.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List follower or create new if user is logged in.
    """

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieving a follower, delete (unfollow) if user is owner.
    """

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
