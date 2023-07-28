from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.blog.models import Category, Blog, Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentSerializer
from apps.common.permissions import ReadOnly


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        blog_data = BlogSerializer(blog).data

        
        comments = Comment.objects.filter(blog=blog)
        comment_data = CommentSerializer(comments, many=True).data

    
        blog_data['comments'] = comment_data
        return Response(blog_data)

class CommentCreateView(GenericAPIView):
    serializer_class = CommentSerializer 

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)