from django.test import TestCase, Client
from django.core.cache import cache

class TranslationAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_sentence_translation(self):
        # Test case for translating a single sentence
        response = self.client.get('/translate/', {'source_language': 'en', 'target_language': 'es', 'text': 'Hello'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['translation'], 'Hola')

    def test_paragraph_translation(self):
        # Test case for translating a paragraph
        response = self.client.get('/translate/', {'source_language': 'en', 'target_language': 'fr', 'text': 'This is a test paragraph.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['translation'], 'Ceci est un paragraphe test.')

    def test_cache_hit(self):
        # Test case to check if translation is served from cache
        # First, store a translation in the cache
        cache.set('en-es-Hello', 'Hola', timeout=3600)

        # Make a request for the same translation
        response = self.client.get('/translate/', {'source_language': 'en', 'target_language': 'es', 'text': 'Hello'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['translation'], 'Hola')

    def test_cache_miss(self):
        # Test case to check if translation is not served from cache
        # Clear any existing translation from the cache
        cache.delete('en-es-Hello')

        # Make a request for a translation that is not in the cache
        response = self.client.get('/translate/', {'source_language': 'en', 'target_language': 'es', 'text': 'Hello'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['translation'], 'Hola')
