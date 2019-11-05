import unittest

from django.shortcuts import reverse
from django.test import Client, TestCase

from ..models import Document


class WikiViewsTestCase(TestCase):

    def setUp(self):
        self.doc = Document.objects.create(title='hello doc', slug='hello-slug')

    def test_document_view(self):
        c = Client()
        res = c.get(f'/wiki/doc/{self.doc.slug}/')
        assert res.status_code == 200

    def test_document_create_view_redirect(self):
        c = Client()
        res = c.post('/wiki/create/', data={'title': 'this is a title', 'slug': 'this-slug'})
        assert res.status_code == 302
