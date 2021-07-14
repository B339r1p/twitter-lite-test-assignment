from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from tweets.views import LikeViewSet, RetweetViewSet, TweetViewSet, UserViewSet, index, CommentViewSet

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'retweets', RetweetViewSet)
router.register(r'users', UserViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path("index/", index),
    path("", include(router.urls))
]