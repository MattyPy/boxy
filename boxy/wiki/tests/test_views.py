import unittest
from django.test import Client, TestCase


class WikiViewsTestCase(TestCase):
    def test_document_view(self):
        c = Client()
        res = c.get('/wiki/doc/')
        assert res.status_code == 200

    def test_document_create_view_redirect(self):
        c = Client()
        res = c.post('/wiki/create/', data={'title': 'this is a title', 'slug': 'my-slug'})
        assert res.status_code == 302
