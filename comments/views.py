from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from catch_chronicle.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentsDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List of comments, create new comment if user is logged in.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['catch']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieving a comment, update or delete if user is owner.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
