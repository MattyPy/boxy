from django.db import models
import uuid
# Create your models here.


class Document(models.Model):

    title = models.CharField(max_length=255)

    slug = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.get_absolute_url()}, ({self.title})'

    def get_absolute_url(self):
        return f'/wiki/doc/{self.slug}/'


class Revision(models.Model):

    content = models.TextField()
