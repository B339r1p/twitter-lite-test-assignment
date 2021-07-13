from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tweet(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    @admin.display(description='Likes')
    def get_num_of_likes(self):
        return Like.objects.filter(tweet=self).count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # this makes sure that the user and tweet pair don't occur more than once
        # e.g. (user1, tweet1) can only exist once
        unique_together = ('user', 'tweet',)

class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

