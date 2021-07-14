from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Like, Retweet, Tweet, Comment
from rest_framework.serializers import ModelSerializer

class TweetSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    likes = serializers.IntegerField(source='get_num_of_likes', read_only=True)

    class Meta:
        model = Tweet
        fields = ["text", "username", "likes", "created_on", "user"]

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["tweet", "user"]


class RetweetSerializer(ModelSerializer):
    class Meta:
        model = Retweet
        fields = ["tweet", "user"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'