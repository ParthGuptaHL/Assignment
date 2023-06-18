from googletrans import Translator
from django.core.cache import cache
from django.http import JsonResponse
import hashlib

#View to accept query params and translate text
def translate_text(request):
    #Extract source language, target language and text to be translated from our API call
    source_language = request.GET.get('source_language')
    target_language = request.GET.get('target_language') 
    text = request.GET.get('text')

    #Stores queries in cache encrypted with proper md5 hash
    cache_key = hashlib.md5(f'{source_language}-{target_language}-{text}'.encode()).hexdigest()
    translation = cache.get(cache_key)

    #Calls the Google Translate API if the query doesn't already exist in cache
    if translation is None:
        translator = Translator()
        translation = translator.translate(text, src=source_language, dest=target_language).text
        #Adds the result to the cache
        cache.set(cache_key, translation)

    return JsonResponse({'translation': translation})
