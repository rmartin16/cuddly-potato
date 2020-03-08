from django.urls import path

from . import views

urlpatterns = [
    path('<str:show_abbrev>/rss', views.PodcastFeed(), name='podcast-feed'),
    path('<str:show_abbrev>/episodes/<str:episode_uuid>', views.episode_file, name='podcast-episode')
]
