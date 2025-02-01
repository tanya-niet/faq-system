# faq_system/models.py

from django.db import models

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    # Translated fields for different languages
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_hi = models.TextField(null=True, blank=True)
    answer_bn = models.TextField(null=True, blank=True)

    def get_translated(self, lang='en'):
        # Based on the language, return the translated question and answer
        if lang == 'hi':
            return {
                "question": self.question_hi or self.question,  # Use Hindi or fallback to English
                "answer": self.answer_hi or self.answer,
            }
        elif lang == 'bn':
            return {
                "question": self.question_bn or self.question,  # Use Bengali or fallback to English
                "answer": self.answer_bn or self.answer,
            }
        return {
            "question": self.question,
            "answer": self.answer,
        }

    def __str__(self):
        return self.question
