from django.db import models

# Create your models here.
class YoutubeVideo(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField()

    def __str__(self):
        return self.title
    
