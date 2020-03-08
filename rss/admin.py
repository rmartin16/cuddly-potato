from django.contrib import admin

from .models import Podcast
from .models import PodcastEpisode

admin.site.register(Podcast)
admin.site.register(PodcastEpisode)
