from django.db import models
import uuid

from feeder.settings import IMAGES_DIR, EPISODES_DIR


class Podcast(models.Model):
    name = models.CharField(max_length=254)
    abbreviation = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    cover_art = models.FilePathField(path=str(IMAGES_DIR), max_length=254, recursive=True, )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class PodcastEpisode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    description = models.TextField()
    media = models.FilePathField(path=str(EPISODES_DIR), max_length=254, recursive=True)
    pub_date = models.DateTimeField(verbose_name='publication date')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{self.podcast.name} - {self.title}'
