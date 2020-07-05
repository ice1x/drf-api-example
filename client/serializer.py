from rest_framework import serializers


class PostsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    url = serializers.CharField(max_length=256)
    title = serializers.CharField(max_length=256)
    created = serializers.DateTimeField()
