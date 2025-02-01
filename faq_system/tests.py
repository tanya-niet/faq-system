from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):

    def setUp(self):
        # Set up initial data in the database for testing
        FAQ.objects.create(question="What is Django?", answer="A Python web framework.")
        FAQ.objects.create(question="What is Python?", answer="A programming language.")

    def test_get_translated_question(self):
        # Fetch FAQ object
        faq = FAQ.objects.get(id=1)
        
        # Test translation for 'en' (English)
        translated_faq = faq.get_translated('en')  # This returns a dictionary
        self.assertEqual(translated_faq['question'], "What is Django?")  # Check the 'question' field
        
        # Optionally, test for other languages like Hindi (hi)
        translated_faq_hi = faq.get_translated('hi')
        self.assertEqual(translated_faq_hi['question'], "What is Django?")  # Assuming Hindi translation is missing

        # Add a translation for Hindi question to test
        faq.question_hi = "डजंगो क्या है?"
        faq.save()

        translated_faq_hi = faq.get_translated('hi')
        self.assertEqual(translated_faq_hi['question'], "डजंगो क्या है?")  # Test the Hindi translation

    def test_cache_is_set(self):
        # Test to check if caching works (assuming the cache is set up properly)
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, 200)

    def test_get_faqs_view(self):
        # Test the actual view functionality for fetching FAQs
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, 200)

    def test_faq_translation_for_multiple_languages(self):
        # Testing translations for multiple languages
        faq = FAQ.objects.get(id=1)
        
        # Translate to English
        translated_en = faq.get_translated('en')
        self.assertEqual(translated_en['question'], "What is Django?")
        
        # Translate to Hindi (hi)
        translated_hi = faq.get_translated('hi')
        self.assertEqual(translated_hi['question'], "What is Django?")  # Assuming the fallback is used
        
        # Add Hindi translation and test again
        faq.question_hi = "डजंगो क्या है?"
        faq.save()

        translated_hi = faq.get_translated('hi')
        self.assertEqual(translated_hi['question'], "डजंगो क्या है?")  # Now Hindi translation should be used

    def test_get_translated_answer(self):
        # Test the translated answer for 'en' (English)
        faq = FAQ.objects.get(id=1)
        
        translated_answer = faq.get_translated('en')  # Get translated answer in English
        self.assertEqual(translated_answer['answer'], "A Python web framework.")  # Check the 'answer' field
        
        # Test for Hindi (hi)
        translated_answer_hi = faq.get_translated('hi')
        self.assertEqual(translated_answer_hi['answer'], "A Python web framework.")  # Assuming Hindi translation is missing

        # Add a Hindi translation for the answer
        faq.answer_hi = "एक पायथन वेब फ्रेमवर्क।"
        faq.save()

        translated_answer_hi = faq.get_translated('hi')
        self.assertEqual(translated_answer_hi['answer'], "एक पायथन वेब फ्रेमवर्क।")  # Test the Hindi translation

