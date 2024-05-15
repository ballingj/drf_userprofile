from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """An example API View format"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns one or more items"""
        my_list = [list1, list2, list3]
        return Response({
          'item': 'item1',
          'list': my_list,
        })

    def post(self, request, format=None):
        """Create a new item"""
        return Response({'new': 'item'})
  

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'updated': 'item'})


    def patch(self, request, pk=None):
        """Handle partial update of object"""        
        return Response({'partially_updated': 'item'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'deleted': 'item'})

