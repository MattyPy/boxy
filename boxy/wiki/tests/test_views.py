import unittest
from django.test import Client, TestCase


class WikiViewsTestCase(TestCase):
    def test_document_view(self):
        c = Client()
        res = c.get('/wiki/doc/')
        assert res.status_code == 200
