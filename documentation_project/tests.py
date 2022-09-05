from django.test import TestCase
import os
from django.contrib.auth.password_validation import validate_password


class TryDjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        is_string = validate_password(SECRET_KEY)
        self.assertEqual(is_string, None)
