from django.db import models
import uuid
# Create your models here.


class Document(models.Model):

    title = models.CharField(max_length=255)

    slug = models.CharField(max_length=255)

    def get_absolute_url(self):
        return f'/wiki/doc/{self.slug}/'
