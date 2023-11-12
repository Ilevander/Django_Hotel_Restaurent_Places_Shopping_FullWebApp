from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.shortcuts import get_object_or_404
from django.db.models.query_utils import Q  
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated]) #To let the data json accompagned with a token as portal the get or post any data from the backend to the frontend or reverse as a part of security
def post_list_api(request):
    all_posts = Post.objects.all()
    data = PostSerializer(all_posts,many=True).data 
    return Response({'data':data})
#using this url to go to the url : http://127.0.0.1:8000/blog/api/list


@api_view(['GET'])
@permission_classes([IsAuthenticated])

def post_detail_api(request,id):
    post = get_object_or_404(Post,id=id)
    data = PostSerializer(post).data 
    return Response({'data':data})
#using this url to go to the url : http://127.0.0.1:8000/blog/api/list/id=1 or 2 or 3....


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_search_api(request,query):
    posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    data = PostSerializer(posts,many=True).data 
    return Response({'data':data})