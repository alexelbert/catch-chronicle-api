from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Catch
from .serializers import CatchSerializer
from catch_chronicle.permissions import IsOwnerOrReadOnly


class CatchList(generics.ListCreateAPIView):
    """
    List catches or create a new catch if logged in.
    """
    serializer_class = CatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Catch.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CatchDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a catch if you own it.
    """
    serializer_class = CatchSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Catch.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

