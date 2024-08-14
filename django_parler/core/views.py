from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import BlogPost
from .serializers import BlogPostSerializer
from .filters import BlogPostFilter

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogPostFilter
