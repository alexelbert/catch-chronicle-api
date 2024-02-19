from rest_framework import generics, permissions
from catch_chronicle.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List of all likes, logged in user can make a new like. 
    """
    
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieving a like, update or delete if user is owner.
    """
    
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
