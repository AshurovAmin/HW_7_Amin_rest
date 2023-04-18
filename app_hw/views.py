from rest_framework import generics

from . models import Comment, Tweet, Mark
from .serializers import CommentSerializer, TweetSerializer, MarkSerializer


class TweetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MarkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


