from django.contrib import admin
from .models import FAQ
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.core.cache import cache

# Create a custom form to use CKEditor widget for the 'answer' field
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditorWidget(),  # Apply CKEditor to 'answer' field
        }

# Register the FAQ model with the custom form in the admin panel
class FAQAdmin(admin.ModelAdmin):
    form = FAQForm

    # Override the save_model method to clear cache when an FAQ is updated
    def save_model(self, request, obj, form, change):
        # If an FAQ is updated, clear its cache
        lang = 'en'  # Default to 'en' or dynamically handle this if needed
        cache_key = f"faqs_{lang}"
        cache.delete(cache_key)
        super().save_model(request, obj, form, change)

# Register the FAQ model in the admin panel with the FAQAdmin class
admin.site.register(FAQ, FAQAdmin)

