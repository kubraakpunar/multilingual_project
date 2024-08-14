from rest_framework import filters
from django.db.models import Q

TRANSLATION_TABLE = str.maketrans({
        'ş': 's', 'Ş': 'S',
        'ı': 'i', 'I': 'i',
        'ç': 'c', 'Ç': 'C',
        'ü': 'u', 'Ü': 'U',
        'ö': 'o', 'Ö': 'O',
        'ğ': 'g', 'Ğ': 'G',

    })

def normalize_query(query):
    return query.translate(TRANSLATION_TABLE).lower()

class CustomSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_param = request.query_params.get('search', None)
        if search_param:
            normalized_query = normalize_query(search_param)
            
            queryset = queryset.filter(
                Q(translations__title__unaccent__icontains=normalized_query)  |
                Q(translations__content__unaccent__icontains=normalized_query)
            )
        return queryset
