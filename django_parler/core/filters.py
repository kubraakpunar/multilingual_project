import django_filters
from .models import BlogPost
from django.db.models import Q
from unidecode import unidecode

def normalize(value):
    return (value
            .replace('İ', 'I').replace('ı', 'i')
            .replace('ş', 's').replace('Ş', 's')
            .replace('ç', 'c').replace('Ç', 'c')
            .replace('ö', 'o').replace('Ö', 'o')
            .replace('ü', 'u').replace('Ü', 'u')
            .replace('ğ', 'g').replace('Ğ', 'g')
            .replace('ı', 'i').replace('I', 'i')
    )

class TurkishCharFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value:
            normalized_value = normalize(value.lower())
            return qs.filter(
                Q(translations__title__icontains=normalized_value) |
                Q(translations__content__icontains=normalized_value)
            )
        return qs

class BlogPostFilter(django_filters.FilterSet):
    search = TurkishCharFilter(field_name='translations__title')

    class Meta:
        model = BlogPost
        fields = ['search']
