from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from tweets.views import LikeViewSet, RetweetViewSet, TweetViewSet, UserViewSet, index

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'retweets', RetweetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path("index/", index),
    path("", include(router.urls))
]