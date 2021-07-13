from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tweets.models import Tweet, Like, Retweet

class TweetTests(APITestCase):
    def test_create_tweet(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="lami", password="password123")

        url = reverse('tweet-list')
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.post(url, data) # format='json'
        response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.get().text, data['text'])
        self.assertEqual(response_data['text'], data['text'])

    
    def test_patch_tweet(self):
        """
        Ensure we can patch the tweet object.
        """

        user = User.objects.create_user(username="lami", password="password123")
        tweet = Tweet.objects.create(text=" SpaceX_project loading...... ", user=user)

        url = reverse('tweet-detail', kwargs={'pk':tweet.id})
        data = {'text': 'Lami', 'user': user.id}
        response = self.client.patch(url, data)
        response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_tweet(self):
        """
        Ensure we can create a new retweet object.
        """
        user = User.objects.create_user(username="lami", password="password123")
        tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

        url = reverse('retweet-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_tweet(self):
        """
        Ensure we can delete the tweet object.
        """
        user = User.objects.create_user(username="lami", password="password123")
        tweet = Tweet.objects.create(text="No Bill Me", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.delete(url,data, format = 'json')
        # response_data = response.json()
        print(response)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

################################################################################################################3

class RetweetTests(APITestCase):
    def test_create_retweet(self):
        """
        Ensure we can create a new retweet object.
        """
        user = User.objects.create_user(username="lami", password="password123")
        tweet = Tweet.objects.create(text="on God", user=user)

        url = reverse('retweet-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_put_retweet(self):
        """
        Ensure we can create a new retweet object.
        """
        user = User.objects.create_user(username="lami", password="password123")
        tweet = Tweet.objects.create(text="all thanks and adoration be unto the Lord", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'LibertyApps', "user": user.id}
        response = self.client.put(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.get().text, data['text'])
        self.assertEqual(response_data['text'], data['text'])
    

    def test_patch_tweet(self):
        """
        Ensure we can patch the tweet object.
        """
        user = User.objects.create_user(username="lami", password="password123")
        tweet = Tweet.objects.create(text="i like the way am feeling now", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.patch(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_get_retweet(self):

        user=User.objects.create_user(username='j_one',password='password123')
        tweet = Tweet.objects.create(text='God is at work',user=user)

        url= reverse('tweet-list')
        data={'tweet':tweet.id,'user':user.id}
        response= self.client.get(url,data,format='json')
        response_data=response.json()
        print(response_data)

        self.assertEqual(response.status_code,status.HTTP_200_OK)

########################################################################################################################

class LikeTests(APITestCase):
    def test_create_like(self):
        """
        Ensure we can like tweet object.
        """
        user = User.objects.create_user(username="oladapo", password="password123")
        tweet = Tweet.objects.create(text="We are getting there", user=user)

        url = reverse('like-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_get_like(self):
        """
        Ensure we can get tweet object.
        """
        user = User.objects.create_user(username="lami", password="password123")
        tweet = Tweet.objects.create(text="Omooo eh don dey choke oooooo",user=user)

        url = reverse("like-list")
        data ={'tweet':tweet.id, "user":user.id}
        response = self.client.get(url,data,format='json')
        print("done")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_patch_like(self):

        user = User.objects.create_user(username="lami",password="password123")
        tweet = Tweet.objects.create(text="Monday", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'tweet':tweet.id,"user":user.id}
        response = self.client.patch(url,data,format='json')
        print('done')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_delete_like(self):

        user = User.objects.create_user(username='lami', password='password')
        tweet = Tweet.objects.create(text='JesuChristian',user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data= {'tweet':tweet.id,'user':user.id}
        response = self.client.delete(url,data,format='json')
        print('complete')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

