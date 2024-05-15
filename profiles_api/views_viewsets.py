from rest_framework.views import viewsets
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(viewsets.ViewSets):
    """An example API View format"""

    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """List items"""
        my_list = ['item1', 'item2', 'item3']
        return Response({'list': my_list})


    def create(self, request):
        """Create a new item"""
        return Response({'created': 'item'})
  

    def retrieve(self, request, pk=None):
        """Retrieve an item"""
        return Response({'retrieved': 'item'})


    def update(self, request, pk=None):
        """Update an item"""        
        return Response({'updated': 'item'})


    def partial_update(self, request, pk=None):
        """Update part of an item"""        
        return Response({'partially_updated': 'item'})


    def destroy(self, request, pk=None):
        """Delete an item"""
        return Response({'deleted': 'item'})

