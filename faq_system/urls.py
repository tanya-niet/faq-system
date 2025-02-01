# faq_system/urls.py

from django.urls import path
from .views import get_faqs  # Import your view function

urlpatterns = [
    path('api/faqs/', get_faqs, name='get_faqs'),  # Map the URL to the 'get_faqs' view
]
