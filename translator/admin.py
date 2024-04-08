from django.contrib import admin
from .models import TextTranslator

class TextTranslatorAdmin(admin.ModelAdmin):
    list_display = [
        "card",
        "display_card_lan"
        "translated_text",
        "tokens",
        "creation_date",
        "modification_date",
    ]
    def display_card_lan(self, obj):
        return obj.card.lan
    display_card_lan.short_description = 'Lan origin'

    def change_view(self, request, object_id, form_url="", extra_context=None):
        # Get the object instance
        obj = TextTranslator.objects.get(pk=object_id)
        # Pass the instance to the template context
        extra_context = extra_context or {}
        extra_context["instance"] = obj
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context
        )

admin.site.register(TextTranslator, TextTranslatorAdmin)
