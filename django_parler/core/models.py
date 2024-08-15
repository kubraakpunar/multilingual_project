from django.db import models
from parler.models import TranslatableModel,TranslatedFields

class BlogPost(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        content = models.TextField()
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter('title', language_code='tr', any_language=True)