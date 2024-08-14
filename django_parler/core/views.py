from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import BlogPost
from .serializers import BlogPostSerializer
from .filters import CustomSearchFilter
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [CustomSearchFilter]
    search_fields = ['translations__title', 'translations__content']


