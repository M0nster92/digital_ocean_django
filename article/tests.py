from unicodedata import name
from django.test import TestCase

from .models import Article


class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(name='Hello world', content='body')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
