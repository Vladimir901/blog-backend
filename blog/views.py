# import json
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
# from rest_framework import filters, permissions
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response

from .models import *
from .serializers import *

def index(request):
    return HttpResponse("Hello METANIT.COM")

class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    def get_queryset(self):
        req = self.request.query_params
        queryset = Blog.objects.all().order_by("-datetimecreate")
        if req.get("id"):
            queryset = queryset.filter(id=int(req.get("id")))
        if req.get("theme"):
            queryset = queryset.filter(theme=req.get("theme"))
        return queryset
    
    @action(detail=True, methods=['POST'], url_path="save")
    def add_post(self, request, pk=None):
        data = self.request.data
        if int(pk)==0:
            data['id'] = Blog.objects.count()+1
        else:  
            data['id'] = int(pk)

        author = Author.objects.get(id=data['author'])
        post = Blog.objects.update_or_create(id=data['id'], defaults={"theme": data["theme"], "text": data['text'], "author": author, "datetimecreate": data['datetimecreate']})
        
        return Response({'id': post[0].id})
    