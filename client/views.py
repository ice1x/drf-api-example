import datetime
import django_filters
from rest_framework import filters

from rest_framework import generics
from rest_framework.response import Response

from .models import Posts
from .serializer import PostsSerializer


DATE_FORMAT = "%Y-%m-%d"
START_DATE = "2000-01-01"


class PostsView(generics.ListAPIView):
    """
    Stats list view with sorting
    """
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

    def get(self, request, order=None):

        order = request.GET.get('order', '')
        print(f"order: {order}")
        posts = Posts.objects.all()

        if order:
            posts = posts.order_by(order)

        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)
