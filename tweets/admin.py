from tweets.models import Like, Retweet, Tweet, Comment
from django.contrib import admin


# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'get_num_of_likes',)

admin.site.register(Like)
admin.site.register(Retweet)
admin.site.register(Comment)