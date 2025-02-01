from django.http import JsonResponse
from django.core.cache import cache
from .models import FAQ

def get_faqs(request):
    lang = request.GET.get('lang', 'en')  # Default to 'en' if no 'lang' is provided

    # Generate a cache key based on the language
    cache_key = f"faqs_{lang}"

    # Check if the data is in the cache
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data, safe=False)

    # If not in cache, get the FAQs from the database
    faqs = FAQ.objects.all()

    # Prepare the response data with translations
    data = []
    for faq in faqs:
        # Get translated question and answer directly from the model's method
        faq_data = faq.get_translated(lang)  # This method handles the translations
        data.append(faq_data)

    # Cache the data for future use (set timeout to 1 hour, or as needed)
    cache.set(cache_key, data, timeout=3600)

    return JsonResponse(data, safe=False)
