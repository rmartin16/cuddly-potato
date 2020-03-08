from django.urls import path

from . import views

urlpatterns = [
    path('<str:show_abbrev>/rss', views.PodcastFeedView(), name='podcast-feed'),
    path('<str:show_abbrev>/episodes/<str:episode_uuid>', views.episode_file, name='podcast-episode'),
    path('<str:show_abbrev>/art', views.podcast_art, name='podcast-art')
]
