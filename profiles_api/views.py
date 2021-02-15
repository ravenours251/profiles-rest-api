from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .permissions import UpdateOwnProfile,UpdateOwnStatus
from . import serializers
from .models import UserProfile,ProfileFeedItem
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class HelloApiView(APIView):
    """ Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list APIVIEW features"""
        an_apiview = [
            'Uses HHTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Is mapped mannually URLS'
        ]
        
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'methodd':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial Update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """ Delete an object"""
        return Response({'method':'Delete'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset = [
            'Uses action  (List, create, retrieve, update, partial_update',
            'Automatically maps URLs using Rounters',
            'Provides more functionality with less code'
        ]

        return Response({
                         'message':'Hello',
                         'a_viewset':a_viewset,
                       })

    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'Message':message
            })
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({
            'hhtp_method':'GET'
        })

    def update(self,request,pk=None):
        """ Updating an object"""
        return Response({
            'http_method':'PUT'
        })

    def partial_update(self,request,pk=None):
        """Update partial"""
        return Response({
            'http_method':'PATCH'
        })

    def destroy(self,request,pk=None):
        """Destroy an object """
        return Response({
            'http_method':'Delete'
        })  

class ProfileViewSet(viewsets.ModelViewSet):    
    """Handle Creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):    
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handle creating, reading, and updating profile feeds item"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer 
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (
        UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self,serializer):
        """Sets the user profile to logged in USER"""
        serializer.save(user_profile=self.request.user)