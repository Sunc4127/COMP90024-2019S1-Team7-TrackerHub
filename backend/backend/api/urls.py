# coding: utf-8

from django.urls import path, re_path
from backend.api.views.tweets import tweet_router
from backend.api.views.tweet_pics import tweet_pic_router


urlpatterns = [
    path('tweet/pic/<str:resource>/', tweet_pic_router),
    path('tweet/pic/', tweet_pic_router),
    path('tweet/', tweet_router),
    path('tweet/<str:resource>/', tweet_router),
]
