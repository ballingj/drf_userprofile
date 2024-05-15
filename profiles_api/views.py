from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated # , IsAuthenticatedOrReadOnly

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
          'Uses HTTP methods as functions (get, post, patch, put, delete)',
          'Is similar to a traditional Django View',
          'Gives you the most control over your logic',
          'Is mapped manually to URLs',
        ]
        
        return Response({
          'message': 'Hello!',
          'an_apiview': an_apiview,
        })

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handle updating an object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({
              'message': message,
              'method': 'PUT'
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def patch(self, request, pk=None):
        """Handle partial update of object"""        
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Returns a Hello message"""
        
        a_viewset = [
          'Uses actions (list, create, retrieve, update, partial_update, destroy)',
          'Automatically maps to URLs using Routers',
          'Provides more functionality with less code',
        ]
        
        return Response({
          'message': 'Hello!',
          'a_viewset': a_viewset,
        })

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle retrieving an object by ID"""
        return Response({'http_method': 'GET'})
        

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})
        

    def partial_update(self, request, pk=None):
        """HAndle updating part of an object"""
        return Response({'http_method': 'PATCH'})
    

    def destroy(self, request, pk=None):
        """Deleted the object"""
        return Response({'http_method': 'DELETE'})


# Using ModelViewSets
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )    # this needs to be a tuple hence the comma
    permission_classes = (permissions.UpdateOwnProfile, )   # also needs to be a tuple

    # add a searcheable filter -- # ussage: <endpoint>/?search=test
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """
    Overall, this code snippet sets up an API endpoint for user login,
    where clients can send their credentials (e.g., username and password)
    to obtain an authentication token. The token can then be included in
    subsequent requests to authenticate the user.
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
        # IsAuthenticatedOrReadOnly
    )
    
    def perform_create(self, serializer):
        """Sets the user profile to the logged-in user"""
        serializer.save(user_profile=self.request.user)


