from django.db import models


class Posts(models.Model):
    """
    date,channel,country,os,impressions,clicks,installs,spend,revenue
    2017-05-17,adcolony,US,android,19887,494,76,148.2,149.04
    """
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    created = models.DateTimeField()
