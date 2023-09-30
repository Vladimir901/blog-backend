from rest_framework import serializers

from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Blog
        fields = '__all__'

