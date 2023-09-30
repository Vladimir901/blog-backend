from django.http import HttpResponse

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

def index(request):
    return HttpResponse("Hello METANIT.COM")

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    def get_queryset(self):
        req = self.request.query_params
        queryset = Blog.objects.all()
        if req.get("theme"):
            queryset = queryset.filter(theme=req.get("theme"))
        return queryset