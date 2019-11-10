import unittest

from django.shortcuts import reverse
from django.test import Client, TestCase, RequestFactory

from boxy.users.tests.factories import UserFactory
from ..models import Document
from ..views import DocumentUpdateview


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
"""
    def test_user_update(self):
        user = UserFactory()
        rf = RequestFactory()
        request = rf.get(reverse('wiki:edit', kwargs={'slug': f'{self.doc.slug}'}))
        request.user = user
        view = DocumentUpdateview()
        view.request = request
        assert view.get_object() == self.doc
"""
