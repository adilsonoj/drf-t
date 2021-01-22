from rest_framework import viewsets
from website.models import Post
from .serializer import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Exibe todos os posts"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer