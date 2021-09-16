import os

from django.apps import AppConfig
from django.db import connection

from feeder.settings import EPISODES_DIR, IMAGES_DIR

class RssConfig(AppConfig):
    name = 'rss'

    def ready(self):
        # runs once when the app is brought up
        if connection.introspection.table_names():
            from django.contrib.sites.models import Site
            site = Site.objects.get_current()
            site.name = os.environ.get('DOMAIN', 'UPDATE_TO_YOUR_DOMAIN.com')
            site.domain = site.name
            site.save()
    
        for dir in (EPISODES_DIR, IMAGES_DIR):
            dir.mkdir(parents=True, exist_ok=True)

