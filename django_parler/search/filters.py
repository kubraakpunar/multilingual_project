from rest_framework import filters
from django.db.models import Q
from text_unidecode import unidecode

def remove_turkish_characters(query):
    
    return unidecode(query).lower()

class TurkishCompatibleSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_term = request.query_params.get('search', None)
        if search_term:
            normalized_term = remove_turkish_characters(search_term)
            
            queryset = queryset.filter(
                Q(translations__title__unaccent__icontains=normalized_term) |
                Q(translations__content__unaccent__icontains=normalized_term)
            )
        return queryset
