from rest_framework import serializers

from .models import Tweet, Mark, Comment


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
