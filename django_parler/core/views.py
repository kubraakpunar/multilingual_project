from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer
from .filters import TurkishCompatibleSearchFilter
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [TurkishCompatibleSearchFilter]
    search_fields = ['translations__title', 'translations__content']


