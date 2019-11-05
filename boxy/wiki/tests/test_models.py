from django.test import TestCase
from django.urls import reverse

from ..models import Document


class WikiModelTest(TestCase):
    def test_document_get_absolute_url(self):
        doc = Document.objects.create(title='title', slug='slug')
        assert doc.get_absolute_url() == reverse('wiki:list', kwargs={'slug': 'slug'})
