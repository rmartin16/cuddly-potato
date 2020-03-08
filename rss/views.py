import os
import datetime

from mutagen.mp3 import MP3

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from django.views.static import serve

from rss.models import Podcast
from rss.models import PodcastEpisode


class PodcastFeed(Rss201rev2Feed):
    def root_attributes(self):
        attrs = super().root_attributes()
        attrs['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
        return attrs

    def add_root_elements(self, handler):
        super().add_root_elements(handler)

    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        handler.addQuickElement('itunes:duration', item['duration'])


class PodcastFeed(Feed):
    feed_type = PodcastFeed

    def get_object(self, request, show_abbrev: str):
        return get_object_or_404(Podcast, abbreviation=show_abbrev)

    def title(self, podcast: Podcast):
        return podcast.name

    def description(self, podcast: Podcast):
        return podcast.description

    def link(self, podcast: Podcast):
        return reverse('podcast-feed', args=(podcast.abbreviation,))

    def items(self, podcast: Podcast):
        return PodcastEpisode.objects.filter(podcast=podcast).order_by('-pub_date')[:25]

    def item_title(self, episode: PodcastEpisode):
        return episode.title

    def item_description(self, episode: PodcastEpisode):
        return episode.description

    def item_pubdate(self, episode: PodcastEpisode):
        return episode.pub_date

    def item_link(self, episode: PodcastEpisode):
        return reverse('podcast-episode', args=(episode.podcast.abbreviation, episode.uuid))

    def item_enclosure_url(self, episode: PodcastEpisode):
        domain = Site.objects.get_current().domain
        return ''.join(
            ['http://', domain, reverse('podcast-episode', args=(episode.podcast.abbreviation, episode.uuid))]
        )

    def item_enclosure_length(self, episode: PodcastEpisode):
        return os.path.getsize(episode.media)

    def item_extra_kwargs(self, item: PodcastEpisode):
        try:
            duration = str(datetime.timedelta(seconds=round(MP3(item.media).info.length)))
        except Exception as e:
            print('Failed to determine episode length')
            print(f' Episode: {item.title}')
            print(f' Error: {repr(e)}')
            duration = 0
        return {'duration': duration}

    item_enclosure_mime_type = "audio/mpeg"


def episode_file(request, show_abbrev: str, episode_uuid: int):
    episode: PodcastEpisode = get_object_or_404(PodcastEpisode, uuid=episode_uuid)
    filepath = episode.media
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
