from rest_framework import serializers
from .models import Post

'''Django REST framework is a powerful and flexible toolkit for building Web APIs.
'''

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        