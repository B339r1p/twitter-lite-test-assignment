from django.contrib.auth.models import User
from django.urls.base import reverse
from tweets.serializers import LikeSerializer, RetweetSerializer, TweetSerializer, UserSerializer
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Like, Retweet, Tweet

# Create your views here.
def index(request):
    return HttpResponse("Hello Liberty")


class TweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class RetweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Retweet.objects.all()
    serializer_class = RetweetSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer